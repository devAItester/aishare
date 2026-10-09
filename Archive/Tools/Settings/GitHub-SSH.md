# GitHub SSH: два аккаунта по папкам

Цель: использовать два GitHub-аккаунта на одном компьютере без смены SSH-ключей вручную. В командах Git остаются обычные адреса:

`git@github.com:OWNER/REPOSITORY.git`

Git выбирает ключ по расположению репозитория.

## Итоговая схема

```text
~/dev/
├── devAItester/  # аккаунт Dev AI Tester
│   ├── aishare/
│   └── ...
└── faebfe/       # аккаунт FAEBFE
    ├── repo/
    └── ...
```

Ключи:

- `~/.ssh/id_ed25519_devaitester` — аккаунт `devAItester`.
- `~/.ssh/id_ed25519` — аккаунт `FAEBFE`.

Файлы конфигурации Git:

- `~/.config/git/accounts/devAItester.gitconfig`
- `~/.config/git/accounts/faebfe.gitconfig`

## 1. Подготовь папки и проверь инструменты

Установи Git и OpenSSH средствами своей системы. Затем выполни:

```bash
git --version
ssh -V
mkdir -p ~/dev/devAItester ~/dev/faebfe
mkdir -p ~/.ssh ~/.config/git/accounts
chmod 700 ~/.ssh
```

Если репозитории уже находятся в этих папках, повторно клонировать их не нужно. Для автоматического выбора ключа репозитории каждого аккаунта должны находиться внутри соответствующей папки. Если хранишь их в других местах, измени пути в условных настройках из шага 5.

## 2. Создай SSH-ключи, только если их ещё нет

Сначала проверь наличие ключей:

```bash
ls -l ~/.ssh/id_ed25519 ~/.ssh/id_ed25519.pub
ls -l ~/.ssh/id_ed25519_devaitester ~/.ssh/id_ed25519_devaitester.pub
```

Если оба файла конкретного ключа уже существуют, не генерируй его заново: новый ключ с тем же именем может перезаписать старый.

Если ключа FAEBFE ещё нет:

```bash
ssh-keygen -t ed25519 -C "FAEBFE GitHub" -f ~/.ssh/id_ed25519
```

Если ключа Dev AI Tester ещё нет:

```bash
ssh-keygen -t ed25519 -C "Dev AI Tester GitHub" -f ~/.ssh/id_ed25519_devaitester
```

На запрос passphrase можно задать парольную фразу. Приватные файлы без расширения `.pub` никому не отправляй и не загружай в GitHub.

## 3. Добавь открытые ключи в соответствующие аккаунты GitHub

Покажи и скопируй открытый ключ FAEBFE:

```bash
cat ~/.ssh/id_ed25519.pub
```

Войди на GitHub именно под аккаунтом **FAEBFE**. Открой Settings → SSH and GPG keys → New SSH key, вставь содержимое файла и сохрани.

Затем покажи ключ Dev AI Tester:

```bash
cat ~/.ssh/id_ed25519_devaitester.pub
```

Войди под аккаунтом **devAItester** и добавь этот ключ в Settings → SSH and GPG keys → New SSH key.

Один и тот же открытый ключ нельзя добавлять как ключ аутентификации в два разных GitHub-аккаунта. У каждого аккаунта здесь свой ключ.

## 4. Настрой SSH

Открой `~/.ssh/config` в редакторе. Сохрани существующие настройки, если они нужны, и добавь следующие блоки. Блок `github.com` задаёт ключ FAEBFE по умолчанию; второй блок — удобный отдельный псевдоним для ручных SSH-проверок.

```sshconfig
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes

Host github-devaitester
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_devaitester
    IdentitiesOnly yes
```

Затем выставь права:

```bash
chmod 600 ~/.ssh/config
chmod 600 ~/.ssh/id_ed25519 ~/.ssh/id_ed25519_devaitester
chmod 644 ~/.ssh/id_ed25519.pub ~/.ssh/id_ed25519_devaitester.pub
```

Если какие-то файлы ключей отсутствуют, не выполняй для них команду `chmod` — сначала создай соответствующий ключ или исключи отсутствующие файлы из команды.

## 5. Настрой автоматический выбор ключа по папке

Создай файл для аккаунта Dev AI Tester:

```bash
cat > ~/.config/git/accounts/devAItester.gitconfig <<'EOF'
[core]
    sshCommand = ssh -i ~/.ssh/id_ed25519_devaitester -o IdentitiesOnly=yes
EOF
```

Создай файл для аккаунта FAEBFE:

```bash
cat > ~/.config/git/accounts/faebfe.gitconfig <<'EOF'
[core]
    sshCommand = ssh -i ~/.ssh/id_ed25519 -o IdentitiesOnly=yes
EOF
```

Добавь условные подключения в глобальный Git config:

```bash
git config --global --replace-all 'includeIf.gitdir:~/dev/devAItester/.path' ~/.config/git/accounts/devAItester.gitconfig
git config --global --replace-all 'includeIf.gitdir:~/dev/faebfe/.path' ~/.config/git/accounts/faebfe.gitconfig
```

Условие `gitdir` действует на Git-репозитории внутри соответствующей папки, включая вложенные каталоги. В репозиториях используются обычные SSH URL; специальный URL с псевдонимом `github-devaitester` не требуется.

Если у конкретного репозитория уже задан локальный `core.sshCommand`, локальное значение имеет приоритет над глобальным условным файлом. Проверь его командой:

```bash
git -C ~/dev/devAItester/aishare config --local --get core.sshCommand
```

Если команда вывела старую настройку, а ты хочешь управлять ключом через папку, удали только это локальное переопределение:

```bash
git -C ~/dev/devAItester/aishare config --local --unset-all core.sshCommand
```

Повтори для других репозиториев, где обнаружится такое переопределение. Не запускай команду, если локального значения нет.

## 6. Настрой существующие репозитории

Для каждого аккаунта размещай репозитории в соответствующей папке:

- `~/dev/devAItester/REPOSITORY` — репозитории аккаунта devAItester.
- `~/dev/faebfe/REPOSITORY` — репозитории аккаунта FAEBFE.

Если репозиторий уже клонирован в правильную папку, ничего делать с ним не нужно. Если клонируешь существующий репозиторий, используй обычный адрес:

```bash
git clone git@github.com:devAItester/aishare.git ~/dev/devAItester/aishare
git clone git@github.com:FAEBFE/REPOSITORY.git ~/dev/faebfe/REPOSITORY
```

Во второй команде замени `REPOSITORY` на реальное имя репозитория. Не клонируй поверх уже существующей папки.

## 7. Проверь, какой ключ выбирает Git

```bash
for account in devAItester faebfe; do
    for dir in "$HOME/dev/$account"/*/; do
        [ -d "$dir/.git" ] || continue
        printf '\n=== %s/%s ===\n' "$account" "$(basename "$dir")"
        git -C "$dir" config --show-origin --get core.sshCommand
    done
done
```

Ожидаемый результат:

- у репозиториев под `devAItester` указан файл `devAItester.gitconfig` и ключ `id_ed25519_devaitester`;
- у репозиториев под `faebfe` указан файл `faebfe.gitconfig` и ключ `id_ed25519`.

## 8. Проверь реальный доступ к GitHub

```bash
for account in devAItester faebfe; do
    for dir in "$HOME/dev/$account"/*/; do
        [ -d "$dir/.git" ] || continue
        printf '\n=== %s/%s ===\n' "$account" "$(basename "$dir")"
        if output=$(git -C "$dir" ls-remote origin HEAD 2>&1); then
            if [ -n "$output" ]; then
                printf 'OK: %s\n' "$output"
            else
                printf 'OK: HEAD отсутствует; репозиторий может быть пустым.\n'
            fi
        else
            printf 'ERROR: %s\n' "$output"
        fi
    done
done
```

`OK` с хешем означает, что Git получил ссылку `HEAD` у удалённого репозитория. Если вывод сообщает, что `HEAD` отсутствует, репозиторий может быть пустым; это не равнозначно ошибке SSH. Строка `ERROR` требует отдельной проверки.

## Важно: SSH-ключ и авторство коммитов — разные настройки

SSH-ключ определяет, под каким GitHub-аккаунтом выполняется доступ к удалённому репозиторию. Автор коммита определяется отдельно настройками `user.name` и `user.email`. При необходимости задай их на уровне аккаунтных Git config-файлов, но используй адрес электронной почты, который должен отображаться в коммитах этого аккаунта.

## Что должно получиться

Обычные команды работают без ручного переключения ключей:

```bash
git fetch
git pull
git push
```

Перед отправкой изменений проверь `git status`, текущую ветку и `git remote -v`. Не добавляй приватные SSH-ключи в репозиторий и не публикуй их содержимое.
