# AAC — Architecture as Code

LikeC4-модель рабочей Linux-среды пользователя: Arch Linux → Wayland → niri → foot → Bash / Yazi / Neovim и связанные инструменты.

Это **не архитектура сайта** и **не проект menu**.

## Что описывается

Модель охватывает несколько слоёв:

1. **Платформа** — MacBook Air, Arch Linux, Linux kernel, systemd, pacman.
2. **Вход в систему** — greetd запускает пользовательскую сессию niri.
3. **Графическая основа** — Wayland protocol; niri — compositor и Wayland server.
4. **Рабочее взаимодействие** — fuzzel как launcher (Super+Space; на клавиатуре Mac это Command+Space), foot как терминал, Bash как shell.
5. **Ввод и управление** — Apple keyboard и trackpad, Linux input subsystem, libinput, нативные жесты niri, клавиатурные привязки и их настройки.
6. **Файлы и редактирование** — Yazi, Neovim, Fresh, Lazy.nvim, yazi.nvim, imv и mpv; Iosevka Nerd Font 10pt.
7. **Общие механизмы** — Wayland clipboard, wl-clipboard, XDG openers, MIME detection.
8. **Хранилища и обмен** — локальная файловая система, локальный checkout dotfiles, GitHub-репозитории dotfiles/aishare; сетевые шары и облака представлены как расширяемые, пока не подтверждённые точки.
9. **Интеграции отображения** — Yazi выводит Sixel preview в foot; изображения открываются в imv, видео — в mpv.

## Важные технические разграничения

- Wayland — протокол и архитектура взаимодействия, а не отдельный оконный менеджер. niri реализует compositor/server; приложения выступают клиентами.
- foot — Wayland-native terminal emulator. Он запускает shell и TUI-программы внутри терминала.
- Yazi — самостоятельный TUI-файловый менеджер. В обычном сценарии он работает внутри foot.
- Связка Yazi → foot использует Sixel для предпросмотра изображений в терминале.
- Отдельный opener Yazi запускает imv для изображений; прочие файлы открываются через XDG opener.
- Neovim — редактор; Lazy.nvim управляет плагинами; yazi.nvim связывает Neovim с отдельным процессом Yazi. Ранее настроенные вызовы yazi.nvim: Space--, Space-cw и Ctrl+↑; netrw оставлен включённым.
- Sixel в foot не означает, что Sixel-preview автоматически работает внутри встроенного terminal buffer Neovim. Для yazi.nvim это отдельный путь отображения.
- wl-clipboard предоставляет CLI `wl-copy` / `wl-paste` для Wayland clipboard. Primary selection остаётся отдельным механизмом от обычного clipboard.
- Ввод не сводится к жестам: физическая клавиатура и трекпад проходят через Linux input subsystem и libinput к niri. В dotfiles заданы XKB `us,ru`, `grp:caps_toggle`, `tap`, `natural-scroll`, `Mod=Super` и `mod-key-nested=Alt`.
- Niri имеет встроенные touchpad-жесты: три пальца вверх/вниз — смена workspace, три пальца влево/вправо — движение по горизонтальному tiling view, четыре пальца вверх/вниз — overview. В `gestures {}` текущий конфиг только отключает hot corners; отдельного жестового демона или пользовательских swipe-bindings в изученном конфиге нет.
- Клавиатурные привязки — самостоятельный слой управления. `Super+Space` запускает fuzzel, `Super+Return` — foot, `Super+Slash` — foot с Fresh workflow, `Super+1..9` выбирает workspace. Стрелочные привязки управления окнами намеренно отсутствуют.
- **Обнаруженное расхождение:** текущий dotfiles snapshot задаёт `EDITOR=fresh` и `VISUAL=fresh` в `/etc/profile.d/99-editor.sh`, а не Neovim. Niri также передаёт эти значения в D-Bus/systemd. Live state нужно сверить отдельно.
- Yazi использует `$EDITOR` для текстовых файлов, `imv-dir` для изображений, `mpv` для видео и `xdg-open` для остальных файлов согласно текущему `yazi.toml`.

## Статусы модели

- `#confirmed` — компонент или выбор подтверждён в предыдущей работе.
- `#configured` — настройка явно присутствует в проверенном конфигурационном файле; это не гарантирует, что live-система сейчас использует именно эту копию.
- `#supporting` — вспомогательный компонент или утилита.
- `#to-verify` — связь или текущее состояние конфигурации нужно перепроверить на машине.
- Внешние хранилища без подтверждённого провайдера или endpoint обозначены `#to-verify`; наличие узла на диаграмме не означает, что share или cloud mount уже настроен.

Теги не означают, что live-система была проверена. В этой итерации прочитан публичный snapshot `devAItester/dotfiles`; это подтверждает содержимое репозитория, но не гарантирует совпадение с файлами на работающей машине.

## Структура

- `likec4.config.json` — конфигурация LikeC4.
- `specification.c4` — типы элементов, связей и статусов.
- `model.c4` — единственный источник компонентов и связей.
- `views.c4` — статические представления и динамические сценарии из общей модели.
- Введены отдельные типы для устройств ввода, обработчика событий, конфигураций, механизмов взаимодействия, файловых систем, репозиториев и внешних storage targets.

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
| Fresh | `~/.config/fresh/` и `EDITOR/VISUAL` в shell environment |
| Input and gestures | `~/.config/niri/config.kdl` |
| Yazi openers | `~/.config/yazi/yazi.toml` |
| SSH endpoints | `~/.ssh/config` |
| Local/remote mounts | `/etc/fstab`, `/etc/systemd/system/*.mount`, `*.automount` — наличие нужно проверить на машине |
| systemd user services | `~/.config/systemd/user/` |

Пути перечислены как точки конфигурации. В этой итерации фактически прочитаны `niri/config.kdl`, `yazi/yazi.toml`, `yazi/keymap.toml`, `nvim/init.lua`, `/etc/profile.d/99-editor.sh` и `~/.ssh/config` из публичного dotfiles snapshot. В дереве dotfiles не обнаружены `/etc/fstab`, mount/automount units, конфиги rclone/Syncthing или provider-specific cloud clients. Это не доказывает их отсутствие в работающей системе: репозиторий хранит только выбранные конфиги.

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
- NetworkManager — https://networkmanager.dev/docs/
- niri input configuration — https://niri-wm.github.io/niri/Configuration%3A-Input.html
- niri gestures — https://niri-wm.github.io/niri/Gestures.html
- libinput gestures — https://wayland.freedesktop.org/libinput/doc/latest/gestures.html
- systemd.mount — https://www.freedesktop.org/software/systemd/man/latest/systemd.mount.html
- systemd.automount — https://www.freedesktop.org/software/systemd/man/latest/systemd.automount.html
- ArchWiki filesystems — https://wiki.archlinux.org/title/file_systems
- rclone documentation — https://rclone.org/docs/
- Git distributed version control — https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control.html

## Continuous integration and publication

The repository workflow `.github/workflows/pages.yml` runs on pushes and pull requests targeting `main`.

It performs these steps:

1. Builds the existing Jekyll website into `_site/`.
2. Runs `npx likec4@1.60.0 validate` against this directory.
3. Builds the interactive LikeC4 website into `_site/aac/`.
4. Publishes the combined result to GitHub Pages after a push to `main`.

The published interactive architecture is available at:

https://devaitester.github.io/aishare/aac/

The LikeC4 app is built with the repository subpath as its base URL, so its scripts and assets resolve correctly under GitHub Pages.

GitHub Pages accepted the workflow deployment successfully. Jekyll remains the root site and LikeC4 is published under `/aac/`; the generated site is built as one artifact so neither output overwrites the other.

Official references:
- LikeC4 CLI static build: https://likec4.dev/tooling/cli/
- GitHub Pages custom workflows: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

## Проверка

Проверка в GitHub Actions: [run #5](https://github.com/devAItester/aishare/actions/runs/42411056083).

- Jekyll build: success.
- LikeC4 validate (1.60.0): success.
- LikeC4 static build: success.
- Pages artifact upload: success.
- GitHub Pages deployment: success.

Локальная интерактивная проверка в браузере пользователя не выполнялась. Модель проходит автоматическую синтаксическую и layout-проверку; соответствие всех связей реальному состоянию конфигураций ещё требует аудита dotfiles.


## Input architecture and audit

The input model distinguishes physical devices, kernel event delivery, libinput processing, compositor interpretation, native gestures, and keyboard shortcut dispatch. The current niri configuration snapshot specifies:

- Keyboard: XKB layout `us,ru`, option `grp:caps_toggle`, `track-layout "window"`.
- Modifier model: `mod-key "Super"`, `mod-key-nested "Alt"`.
- Touchpad: `tap`, `natural-scroll`.
- Gesture configuration block: `hot-corners { off }`.
- Native niri gestures documented upstream: three-finger vertical workspace switch, three-finger horizontal view movement, four-finger vertical overview toggle.
- Keyboard actions: `Mod+Space` → fuzzel; `Mod+Return` → foot; `Mod+Slash` → foot + Fresh workflow; `Mod+1..9` → workspace selection; media, brightness and screenshot bindings are also configured.
- No Super+arrow window-navigation bindings are present; the config explicitly reserves those keys for applications.

The swipe actions are built into niri. The `gestures {}` section does not define those swipes; it only disables hot corners in this snapshot. Do not invent a separate gesture daemon or per-gesture configuration file.

## Storage and sharing architecture

The storage layer distinguishes local filesystems, the local `~/dotfiles` checkout, the remote `devAItester/dotfiles` repository, and the remote `devAItester/aishare` shared archive. Optional network shares (SMB/NFS/etc.) and cloud storage providers are represented as extension points, not confirmed active mounts.

The reviewed dotfiles tree contains SSH configuration for GitHub and two SSH host aliases (`hh`, `hhh`), but those aliases do not prove that either endpoint is a file server. Earlier package inventory listed `cifs-utils`, `smbclient` and `rsync`; current installation and actual use need a live check. No `fstab`, systemd mount/automount unit, rclone config, Syncthing config or cloud-provider configuration was found in the reviewed repository tree.

For any future share, model the complete path:
`provider/server → protocol/client → mount or sync mechanism → local mountpoint/cache → applications and user workflows`.
A systemd `.mount` unit and `.automount` unit are different roles. Cloud clients may expose a FUSE mount, perform explicit sync, or use an application/API without mounting a filesystem; these architectures must not be collapsed into one generic “cloud” arrow.

## New architecture views

- **Input** — physical devices through kernel/libinput to niri, plus key bindings and native gestures.
- **Storage** — local filesystem, local dotfiles checkout, GitHub remotes and unverified network/cloud extension points.
- **Dynamic input flows** — trackpad gesture processing and keyboard shortcut dispatch.
- **Dynamic storage flow** — local dotfiles checkout to GitHub remote.

## Audit limits and next checks

This is a repository-snapshot audit, not a live machine inventory. Before marking storage nodes as configured, inspect on the workstation:

- `findmnt --real` and `findmnt -t cifs,nfs,nfs4,fuse.rclone`;
- `/etc/fstab` and `systemctl list-units --type=mount --type=automount`;
- `systemctl list-unit-files --type=mount --type=automount`;
- `lsblk -f` and `findmnt -T "$HOME"`;
- installed packages and running processes for SMB/NFS/rclone/Syncthing/provider clients;
- `libinput list-devices` and `libinput debug-events` output.

These are audit targets only; no system commands or configuration changes were executed as part of this repository update.
