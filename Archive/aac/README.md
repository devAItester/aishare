# AAC — Architecture as Code

# Architecture foundation

## Purpose and scope

This model describes a **personal computing environment**, not just one laptop, one Linux installation or a list of installed applications. Its starting point is the user's required capabilities and workloads. Hardware, operating systems, applications, networks and external services are implementation choices used to satisfy those requirements.

The model is intentionally navigable at different levels of detail. The first view should remain small; detailed relationships belong in focused views. Do not add every dependency to the overview.

## Navigation

1. **Personal computing environment** — context: the user, the overall environment and the external service ecosystem.
2. **Architecture foundation** — five domains and their main responsibilities.
3. **Current Arch workstation** — one concrete implementation, with its own focused views for session, input, software and storage.

The existing workstation model is retained as a detailed implementation, not treated as the whole architecture.

## Five architecture domains

| Domain | Responsibility |
|---|---|
| **Requirements & Workloads** | User goals, capabilities, use cases, hard constraints, preferences and quality attributes. |
| **Compute & Platform** | Physical/virtual hardware, operating systems, distribution profiles, installation, kernels, drivers and platform services. |
| **Software & Access** | Applications, alternative clients, interaction methods, protocols and integrations used to deliver capabilities. |
| **Data & External Services** | Local/remote data, repositories, media, network resources, communication and social platforms, AI providers and other external services. |
| **Lifecycle & Knowledge** | Build, install, configure, update, migrate, observe, diagnose, document, recover and preserve operational knowledge. |

These are architectural domains, not a rigid inventory taxonomy. A resource may participate in several domains. For example, a repository can be a data store, a collaboration space and a knowledge base; its roles should be modelled without duplicating the underlying resource.

## Requirement-to-implementation reasoning

A capability is not the same thing as an application or a service. Model the chain only as far as it is useful:

`user need → capability / workload → service or resource → access method → software and platform → compute and hardware`

This is a reasoning path, not a mandatory one-way dependency. There may be several alternative access paths, and a limitation at any point can force a change elsewhere.

Hardware selection is therefore validated against the complete workload: memory, CPU/GPU, storage, display outputs and modes, wireless hardware, audio interfaces, supported operating systems and peripheral connectivity. A replacement device may be justified by a specific unmet requirement rather than by a general desire to upgrade.

## Decision and constraint model

Every significant choice should be recorded with its rationale and status. Keep requirements separate from implementation facts.

| Classification | Meaning |
|---|---|
| **Mandatory** | A hard requirement. A candidate that fails it is excluded. |
| **Preferred** | Strong preference; a compromise is possible with an explicit reason. |
| **Optional** | Useful but not required. |
| **Constraint** | A limitation imposed by hardware, OS, protocol, service, licensing, cost, network access or policy. |
| **Trade-off** | A documented balance between competing requirements. |
| **Unverified** | A hypothesis or current-state assumption that still needs evidence. |

For software candidates, evaluate at least: functional fit, shortcut/gesture compatibility, protocol and OS support, implementation language/runtime, dependencies, resource use, security/privacy, maintenance, licensing, cost and network availability. A preference for a language or technology is a selection criterion, not automatically a hard exclusion unless explicitly marked mandatory.

Alternative applications should remain visible with their current status and the reason they were not selected. Re-evaluate them when the original limitation changes; do not treat a rejected candidate as permanently unsuitable.

## Cross-domain change impact

A change should trigger review only of the connected requirements and decisions, not a wholesale redraw. Examples:

- A new service or communication channel can introduce OS, browser/client, network, privacy and hardware requirements.
- A new display or audio workflow can change GPU, ports, resolution, codec, filesystem and application requirements.
- A change in editor or terminal can affect keyboard mappings, mouse/trackpad interaction, graphics protocols and file-manager integration.
- A new AI provider can change network routes, authentication, cost, data handling and the balance between local and remote compute.
- A storage-format or location change can affect applications, media playback, backup, synchronization and available capacity.

## Modelling and diagram rules

- Keep the context view to a few elements and meaningful relationships.
- Use one view for one question. Avoid a single all-inclusive diagram.
- Prefer navigation into a domain over adding more nodes to the overview.
- Show only relationships that explain a dependency, data flow, control flow or important constraint.
- Do not draw speculative relationships as facts; mark them unverified.
- Distinguish the desired architecture from the currently implemented state.
- Keep decision criteria and rationale attached to the affected choice, rather than turning the main diagram into a legend of every preference.

## C4 and the modelling tool

C4 is a way to describe software architecture at progressively deeper levels: system context, containers, components and code. It also defines supporting views such as system landscape, dynamic and deployment diagrams. **Structurizr** is the C4 creator's reference modelling tool and uses its own DSL to generate multiple views from one model.

This project currently uses **LikeC4**, not Structurizr. LikeC4 provides a code-based model and interactive views. The wider personal computing environment is broader than a conventional software system, so the model uses C4-inspired hierarchy and navigation without forcing every physical, operational or user-requirement concept into a strict C4 container/component category.

Primary references:
- C4 model: https://c4model.com/
- C4 diagrams and abstraction levels: https://c4model.com/diagrams
- Structurizr: https://docs.structurizr.com/
- Structurizr DSL: https://docs.structurizr.com/dsl
- LikeC4: https://likec4.dev/


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
- **Трёхпальцевый tap → PRIMARY paste — отдельный сценарий, не swipe-жест.** Foot по умолчанию вставляет PRIMARY по middle-click. Niri config включает `tap`, но не задаёт `tap-button-map`; соответствие трёхпальцевого tap средней кнопке зависит от эффективного значения libinput/niri и должно быть проверено на машине. Поэтому в модели этот поток помечен как условный, а не как доказанно настроенный.
- Клавиатурные привязки — отдельный слой на каждом уровне. Niri: `Super+Space` запускает fuzzel, `Super+Return` — foot, `Super+Slash` — foot с Fresh workflow, `Super+1..9` выбирает workspace. Foot: `Super+C/V` — clipboard, `Alt+Equal/Minus/0` — размер шрифта. Yazi: `p`, `Alt+\\`, `Alt+'`, `Right/Enter`, `t` имеют отдельные действия. Neovim: `Super+S/A/C/X/V/Z/Y`, `Alt+C/V`, `Shift+Left/Right`; отпускание кнопки мыши копирует выделение в PRIMARY. Стрелочные привязки управления окнами в niri намеренно отсутствуют.
- **Потенциальная коллизия:** Foot и Neovim оба назначают `Super+C/V`: в `foot.ini` это terminal-level clipboard actions, а в `init.lua` — Neovim mappings `<D-c>`/`<D-v>` (`D` в Neovim означает Super/Command). Вложенный терминал может перехватить эти комбинации раньше Neovim. Это не исправлял: нужно проверить фактическую маршрутизацию. `Alt+C/V` в Neovim — отдельная альтернатива, не совпадающая с текущими Foot bindings.
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
- Arch manual: foot.ini key bindings — https://man.archlinux.org/man/foot.ini.5.en
- Neovim key mapping notation — https://neovim.io/doc/user/intro.html
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

Последняя проверка и публикация: [GitHub Actions run #26](https://github.com/devAItester/aishare/actions/runs/42413265945), commit `0d4dcbf7b2fc17728151ec20dab50fb4893e0609`.

- Jekyll build: success.
- LikeC4 validate (1.60.0): success.
- LikeC4 static build: success.
- Pages artifact upload: success.
- GitHub Pages deployment: success.

Автоматическая проверка подтверждает синтаксис модели, layout, сборку и deployment. Браузерная визуальная проверка не выполнялась. Сверка публичного snapshot dotfiles проведена; соответствие live-системе, эффективные настройки tap-button-map/clipboard и фактические mount points ещё требуют проверки на машине.


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

- **Input** — physical devices through kernel/libinput to niri, plus compositor-, terminal-, file-manager- and editor-level key bindings and native gestures.
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
- Check effective niri, foot, Yazi and Neovim mappings against their current config files; include any application-level mouse bindings and clipboard/PRIMARY-selection behavior.

These are audit targets only; no system commands or configuration changes were executed as part of this repository update.
