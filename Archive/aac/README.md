# AAC — Architecture as Code

LikeC4-модель рабочей Linux-среды пользователя: Arch Linux → Wayland → niri → foot → Bash / Yazi / Neovim и связанные инструменты.

Это **не архитектура сайта** и **не проект menu**.

## Что описывается

Модель охватывает несколько слоёв:

1. **Платформа** — MacBook Air, Arch Linux, Linux kernel, systemd, pacman.
2. **Вход в систему** — greetd запускает пользовательскую сессию niri.
3. **Графическая основа** — Wayland protocol; niri — compositor и Wayland server.
4. **Рабочее взаимодействие** — fuzzel как launcher (Command+Space), foot как терминал, Bash как shell.
5. **Файлы и редактирование** — Yazi, Neovim, Lazy.nvim, yazi.nvim, imv; Iosevka Nerd Font 10pt.
6. **Общие механизмы** — Wayland clipboard, wl-clipboard, XDG openers, MIME detection.
7. **Интеграции отображения** — Yazi выводит Sixel preview в foot; изображения также открываются во внешнем imv.

## Важные технические разграничения

- Wayland — протокол и архитектура взаимодействия, а не отдельный оконный менеджер. niri реализует compositor/server; приложения выступают клиентами.
- foot — Wayland-native terminal emulator. Он запускает shell и TUI-программы внутри терминала.
- Yazi — самостоятельный TUI-файловый менеджер. В обычном сценарии он работает внутри foot.
- Связка Yazi → foot использует Sixel для предпросмотра изображений в терминале.
- Отдельный opener Yazi запускает imv для изображений; прочие файлы открываются через XDG opener.
- Neovim — редактор; Lazy.nvim управляет плагинами; yazi.nvim связывает Neovim с отдельным процессом Yazi. Ранее настроенные вызовы yazi.nvim: Space--, Space-cw и Ctrl+↑; netrw оставлен включённым.
- Sixel в foot не означает, что Sixel-preview автоматически работает внутри встроенного terminal buffer Neovim. Для yazi.nvim это отдельный путь отображения.
- wl-clipboard предоставляет CLI `wl-copy` / `wl-paste` для Wayland clipboard. Модель отдельно отмечает primary selection; точная реализация жеста трекпада и передача selection между приложениями требуют проверки на текущей конфигурации.

## Статусы модели

- `#confirmed` — компонент или выбор подтверждён в предыдущей работе.
- `#configured` — интеграция была настроена или проверена в предыдущей работе, но файлы конфигурации сейчас повторно не прочитаны.
- `#supporting` — вспомогательный компонент или утилита.
- `#to-verify` — связь или текущее состояние конфигурации нужно перепроверить на машине.

Теги не означают, что текущие файлы конфигурации были проверены в этой задаче. Файлы dotfiles в этой операции не читались, поэтому модель не выдаёт прежние сведения за свежую проверку.

## Структура

- `likec4.config.json` — конфигурация LikeC4.
- `specification.c4` — типы элементов, связей и статусов.
- `model.c4` — единственный источник компонентов и связей.
- `views.c4` — архитектурные представления, построенные из модели.

**Изменения вносить в `model.c4`.** Представления в `views.c4` фильтруют общую модель и не должны дублировать связи вручную.

## Основные конфигурационные точки

| Компонент | Конфигурация / источник |
|---|---|
| greetd | `/etc/greetd/config.toml` |
| niri | `~/.config/niri/config.kdl` |
| foot | `~/.config/foot/foot.ini` |
| Bash | `~/.bashrc` и shell environment |
| Yazi | `~/.config/yazi/` |
| Neovim | `~/.config/nvim/` |
| systemd user services | `~/.config/systemd/user/` |

Пути перечислены как точки конфигурации, а не как утверждение, что все они были заново проверены. Для Yazi ранее использовались настройки показа скрытых файлов, предпросмотра и opener-правил.

## Первичные источники

- Arch Linux — https://archlinux.org/about/
- Wayland architecture — https://wayland.freedesktop.org/
- Wayland protocol — https://wayland.freedesktop.org/docs/book/Protocol.html
- niri documentation — https://niri-wm.github.io/niri/
- Arch manual: foot — https://man.archlinux.org/man/extra/foot/foot.1.en
- Yazi documentation — https://yazi-rs.github.io/docs/
- Yazi installation and dependencies — https://yazi-rs.github.io/docs/installation/
- Neovim documentation — https://neovim.io/doc/user/
- lazy.nvim — https://github.com/folke/lazy.nvim
- yazi.nvim — https://github.com/mikavilpas/yazi.nvim
- wl-clipboard — https://github.com/bugaevc/wl-clipboard
- greetd manual — https://man.archlinux.org/man/greetd.1.en
- systemd — https://systemd.io/
- fuzzel upstream — https://codeberg.org/dnkl/fuzzel
- imv upstream — https://github.com/eXeC64/imv
- wl-clipboard — https://github.com/bugaevc/wl-clipboard
- NetworkManager — https://networkmanager.dev/docs/

## Проверка

LikeC4 CLI в этой задаче не запускался: GitHub-изменения сделаны напрямую в репозитории, локальная рабочая копия не открыта.

В рабочей копии каталога выполнить:

```sh
npx likec4 validate
npx likec4 start
```

Критерий готовности: модель проходит validate, все связи отражают фактические интеграции, а изменения в модели обновляют все соответствующие views.
