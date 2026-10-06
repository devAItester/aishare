# 01 — systemd timer

Самый простой вариант: один user timer периодически запускает скрипт.

Это контрольный тест. Он нужен, чтобы сначала проверить сам механизм Git ↔ GitHub без file watcher.

## Локальная установка

Клонируй тестовую копию:

```bash
git clone git@github.com:devAItester/aishare.git ~/aishare-sync-test
cd ~/aishare-sync-test
mkdir -p dotfiles-sync-tests/01-timer
printf 'initial\n' > dotfiles-sync-tests/01-timer/test.txt
git add dotfiles-sync-tests/01-timer/test.txt
git commit -m 'test: initialize timer sync'
git push
```

Создай user service:

```bash
mkdir -p ~/.config/systemd/user

cat > ~/.config/systemd/user/aishare-sync-01.service <<'EOF'
[Unit]
Description=aishare sync test 01

[Service]
Type=oneshot
WorkingDirectory=%h/aishare-sync-test
ExecStart=/usr/bin/git add -A
ExecStart=/usr/bin/git commit -m "test: automatic sync" --no-edit
ExecStart=/usr/bin/git push
EOF
```

Создай timer на 30 секунд:

```bash
cat > ~/.config/systemd/user/aishare-sync-01.timer <<'EOF'
[Unit]
Description=aishare sync test 01 timer

[Timer]
OnBootSec=10s
OnUnitActiveSec=30s

[Install]
WantedBy=timers.target
EOF
```

Запусти:

```bash
systemctl --user daemon-reload
systemctl --user enable --now aishare-sync-01.timer
systemctl --user status aishare-sync-01.timer
```

## Проверка

Измени тестовый файл:

```printf 'local %s\n' "$(date)" >> ~/aishare-sync-test/dotfiles-sync-tests/01-timer/test.txt
```

Через максимум ~30 секунд проверь:

```bash
git -C ~/aishare-sync-test log -3 --oneline
systemctl --user status aishare-sync-01.service
```

Затем открой файл на GitHub и проверь новый commit.

## Остановка

```bash
systemctl --user disable --now aishare-sync-01.timer
```

## Что проверяем

- работает ли user timer;
- работает ли push по SSH;
- устраивает ли задержка polling;
- насколько приемлем автоматический commit на каждое обнаруженное изменение.

Этот вариант намеренно примитивный. Если он работает, переходим к `02-path-timer`.
