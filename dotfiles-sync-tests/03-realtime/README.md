# 03 — realtime с рубильником

Это эксперимент с целевой моделью:

- обычное состояние: автоматической связи с GitHub нет;
- `on`: локальные изменения автоматически push'ятся;
- `off`: watcher и remote polling выключены;
- удалённые изменения автоматически pull'ятся только при включённом режиме;
- конфликт не разрешается автоматически.

Для первого теста используется отдельная ветка `sync-test-03`, чтобы эксперимент не затрагивал `main`.

## 1. Подготовить ветку

В тестовой копии:

```bash
cd ~/aishare-sync-test
git switch -c sync-test-03
mkdir -p dotfiles-sync-tests/03-realtime
printf 'initial\n' > dotfiles-sync-tests/03-realtime/test.txt
git add dotfiles-sync-tests/03-realtime/test.txt
git commit -m 'test: initialize realtime sync'
git push -u origin sync-test-03
```

## 2. Скрипт push

```bash
mkdir -p ~/.local/bin ~/.config/systemd/user

cat > ~/.local/bin/aishare-sync-03-push <<'EOF'
#!/bin/bash
set -u

cd "$HOME/aishare-sync-test" || exit 1

# Не трогаем репозиторий, если есть незакоммиченные изменения,
# появившиеся не из watcher.
if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "sync-03: working tree is dirty; refusing automatic sync"
    exit 1
fi

git add -A

if git diff --cached --quiet; then
    exit 0
fi

git commit -m "test: realtime local sync"
git push
EOF

chmod +x ~/.local/bin/aishare-sync-03-push
```

## 3. Скрипт pull

```bash
cat > ~/.local/bin/aishare-sync-03-pull <<'EOF'
#!/bin/bash
set -u

cd "$HOME/aishare-sync-test" || exit 1

if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "sync-03: local changes exist; refusing automatic pull"
    exit 1
fi

git fetch origin

LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/sync-test-03)

if [ "$LOCAL" = "$REMOTE" ]; then
    exit 0
fi

if git merge-base --is-ancestor "$LOCAL" "$REMOTE"; then
    git pull --ff-only
    exit 0
fi

echo "sync-03: histories diverged; automatic pull refused"
exit 1
EOF

chmod +x ~/.local/bin/aishare-sync-03-pull
```

## 4. Локальный watcher

```bash
cat > ~/.config/systemd/user/aishare-sync-03-push.service <<'EOF'
[Unit]
Description=aishare realtime local push

[Service]
Type=oneshot
ExecStart=/bin/bash -lc 'sleep 3; ~/.local/bin/aishare-sync-03-push'
EOF

cat > ~/.config/systemd/user/aishare-sync-03-push.path <<'EOF'
[Unit]
Description=aishare realtime local watcher

[Path]
PathModified=%h/aishare-sync-test/dotfiles-sync-tests/03-realtime/test.txt
Unit=aishare-sync-03-push.service

[Install]
WantedBy=default.target
EOF
```

## 5. Remote watcher

Пока используем timer: systemd timer запускает pull-проверку раз в 15 секунд.

```bash
cat > ~/.config/systemd/user/aishare-sync-03-pull.service <<'EOF'
[Unit]
Description=aishare realtime remote pull

[Service]
Type=oneshot
ExecStart=%h/.local/bin/aishare-sync-03-pull
EOF

cat > ~/.config/systemd/user/aishare-sync-03-pull.timer <<'EOF'
[Unit]
Description=aishare realtime remote polling

[Timer]
OnBootSec=10s
OnUnitActiveSec=15s

[Install]
WantedBy=timers.target
EOF
```

Перезагрузи user units:

```bash
systemctl --user daemon-reload
```

## 6. Рубильник

Включение:

```bash
systemctl --user enable --now aishare-sync-03-push.path
systemctl --user enable --now aishare-sync-03-pull.timer
```

Проверка:

```bash
systemctl --user is-active aishare-sync-03-push.path
systemctl --user is-active aishare-sync-03-pull.timer
```

Выключение:

```bash
systemctl --user disable --now aishare-sync-03-push.path
systemctl --user disable --now aishare-sync-03-pull.timer
```

После этого локальная директория продолжает существовать и Git продолжает работать, но автоматического обращения к GitHub нет.

## 7. Тест A — локально → GitHub

Включи рубильник:

```bash
systemctl --user enable --now aishare-sync-03-push.path aishare-sync-03-pull.timer
```

Измени:

```printf 'local %s\n' "$(date)" >> ~/aishare-sync-test/dotfiles-sync-tests/03-realtime/test.txt
```

Через несколько секунд:

```git -C ~/aishare-sync-test log -2 --oneline```

Проверь новый commit на ветке `sync-test-03`.

## 8. Тест B — GitHub → локально

Когда рубильник включён, измени `dotfiles-sync-tests/03-realtime/test.txt` через GitHub.

В течение примерно 15 секунд локальная копия должна получить fast-forward.

Проверь:

```bash
tail -n 5 ~/aishare-sync-test/dotfiles-sync-tests/03-realtime/test.txt
git -C ~/aishare-sync-test status
```

## 9. Тест C — выключенный режим

Выключи:

```bash
systemctl --user disable --now aishare-sync-03-push.path aishare-sync-03-pull.timer
```

После этого измени файл на GitHub.

Локальная копия **не должна** измениться автоматически.

Затем снова включи оба юнита. Если удалённая история является fast-forward, локальная копия должна обновиться.

## 10. Тест D — конфликт

Это обязательный тест перед переносом схемы на реальные конфиги.

1. Выключи realtime.
2. Измени локальный `test.txt`, но не коммить.
3. Измени тот же файл в GitHub и создай commit.
4. Включи realtime.

Ожидаемый результат:

```
sync-03: local changes exist; refusing automatic pull
```

Никакого `reset --hard`, `force push` или молчаливого перезаписывания быть не должно.

## Почему здесь ff-only

Автоматизация не должна выбирать за нас, чья версия правильная. Если локальная и удалённая история разошлись, процесс останавливается.

Git документирует обычный отказ `push`, когда удалённая ветка не является предком локальной; `--force` отключает эту защиту и может привести к потере коммитов. Поэтому в эксперименте `--force` намеренно отсутствует.

## Критерий выбора

После тестов сравни:

1. задержку;
2. число лишних commits;
3. поведение при нескольких быстрых сохранениях;
4. поведение при отключённом рубильнике;
5. поведение при удалённом изменении;
6. поведение при конфликте;
7. простоту диагностики через `systemctl --user status` и `journalctl --user`.

Только после этого переносим победившую схему на реальные dotfiles.
