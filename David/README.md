# David — локальный архив эталона

Эта папка — единое локальное место для сведений об устройстве сайта Devine Lu Linvega / XXIIVV / Oscean. Цель — не обращаться повторно к GitHub и сайту за уже изученными сведениями и не повторять одни и те же исследования.

## С чего начинать

1. [changes.md](changes.md) — единая таблица различий, решений и статусов.
2. [decisions.md](decisions.md) — принятые решения отдельно от неподтверждённых расхождений.
3. [research/findings.md](research/findings.md) — результаты исследований, источники и ограничения.
4. [source/current-main.css](source/current-main.css) — полный снимок актуального CSS оригинала.
5. [source/history-css.md](source/history-css.md) — исторические версии CSS, в том числе до и после появления halftone.
6. [source/reference-pages.md](source/reference-pages.md) — сохранённые HTML-страницы оригинала: About, Oscean, Styleguide, Shavian и другие.
7. [source/original-project.md](source/original-project.md) — оригинальные README, makefile и корневой index.

## Правило работы

Для вопросов, покрытых этим архивом, сначала используй локальные файлы. Не ходи в сеть за уже сохранённым CSS, HTML, историей или выводами. Проверяй upstream только если пользователь спрашивает о более новой версии, нужного файла нет в архиве или текущих данных недостаточно для разрешения конкретного вопроса.

Не смешивай первоисточники и интерпретации: оригинальные файлы сохранены в `source/`, выводы — в `research/`, решения — в `decisions.md`, реестр отличий — в `changes.md`.

## Происхождение снимка

- Upstream: https://github.com/XXIIVV/oscean
- Ветка: `main`
- Коммит снимка на момент сбора: `recorded in source snapshot metadata`
- CSS: `links/main.css`
- Дата сбора: 2026-10-09

Это снимок, не автоматическое зеркало. Если обновляешь архив, укажи новый upstream commit и дату.
