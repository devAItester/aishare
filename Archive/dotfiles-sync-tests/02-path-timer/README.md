# 02 — systemd.path + timer

Здесь локальная сторона событийная:

- изменение файла → `systemd.path` запускает service;
- удалённая сторона проверяется периодическим timer.

Это уже ближе к рабочей схеме.

## Локальная установка

В тестовой копии:

```bash
cd ~/aishare-sync-test
mkdir -p dotfiles-sync-tests/02-path-timer
printf 'initial\n' > dotfiles-sync-tests/02-path-timer/test.txt
git add dotfiles-sync-tests/02-path-timer/test.txt
git commit -m 'test: initialize path sync'
git push
```

Создай service:

```bash
mkdir -p ~/.config/systemd/user

cat > ~/.config/systemd/user/aishare-sync-02-push.service <<'EOF'
[Unit]
Description=aishare sync test 02 local push

[Service]
Type=oneshot
WorkingDirectory=%h/aishare-sync-test
ExecStart=/usr/bin/bash -lc 'sleep 3; git add -A; git diff --cached --quiet && exit 0; git commit -m "test: automatic local sync"; git push'
EOF
```

Создай path unit:

```bash
cat > ~/.config/systemd/user/aishare-sync-02-push.path <<'EOF'
[Unit]
Description=aishare sync test 02 local watcher

[Path]
PathModified=%h/aishare-sync-test/dotfiles-sync-tests/02-path-timer/test.txt
Unit=aishare-sync-02-push.service

[Install]
WantedBy=default.target
EOF
```

Запусти:

```bash
systemctl --user daemon-reload
systemctl --user enable --now aishare-sync-02-push.path
```

## Проверка локального realtime

Измени файл:

```printf 'local %s\n' "$(date)" >> ~/aishare-sync-test/dotfiles-sync-tests/02-path-timer/test.txt
```

Проверь:

```bash
systemctl --user status aishare-sync-02-push.path
systemctl --user status aishare-sync-02-push.service
git -C ~/aishare-sync-test log -3 --oneline
```

После debounce примерно 3 секунды должен появиться commit и push.

## Важный тест

Быстро выполни несколько изменений подряд:

```for i in 1 2 3 4 5; do printf '%s\n' "change $i" >> ~/aishare-sync-test/dotfiles-sync-tests/02-path-timer/test.txt; sleep 0.3; done```

Посмотри:

```bash
git -C ~/aishare-sync-test log -5 --oneline
```

Нас интересует, удалось ли debounce объединить серию сохранений в один commit.

## Удалённая сторона

Для теста измени этот же файл через GitHub. После этого локальная копия сама по себе не обновится: этот вариант пока тестирует только локальный watcher.

Для pull добавим отдельный timer после проверки локального поведения.

## Остановка

```bash
systemctl --user disable --now aishare-sync-02-push.path
```

## Что проверяем

- достаточно ли systemd.path;
- устраивает ли debounce;
- сколько commits получается при реальном редактировании;
- нужен ли отдельный watcher для каждого файла/каталога;
- подходит ли эта модель для будущих dotfiles.
