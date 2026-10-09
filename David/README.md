# David — локальный архив эталона

Эта папка — единое локальное место для сведений об устройстве сайта Devine Lu Linvega / XXIIVV / Oscean. Цель — не обращаться повторно к GitHub и сайту за уже изученными сведениями и не повторять одни и те же исследования.

## С чего начинать

1. [changes.md](changes.md) — единая таблица различий, решений и статусов.
2. [decisions.md](decisions.md) — принятые решения отдельно от неподтверждённых расхождений.
3. [research/findings.md](research/findings.md) — результаты исследований, источники и ограничения.
4. [source/current-main.css](source/current-main.css) — полный снимок актуального CSS оригинала.
5. [source/history-css.md](source/history-css.md) — исторические версии CSS, включая период до и после появления halftone.
6. [source/pages/styleguide.html](source/pages/styleguide.html) — полная копия HTML Styleguide, демонстрирующая типовые элементы и пустой третий список навигации.
7. [source/reference-pages.md](source/reference-pages.md) — локальные исследовательские выдержки по About, Oscean, Shavian и другим страницам.
8. [source/original-project.md](source/original-project.md) — описание исходного README, Makefile и корневого index.
9. [source/assets/halftone.md](source/assets/halftone.md) — идентификатор и происхождение фонового GIF.

## Правило работы

Для вопросов, покрытых этим архивом, сначала используй локальные файлы. Не ходи в сеть за уже сохранённым CSS, историей или выводами. Проверяй upstream только если пользователь спрашивает о более новой версии, нужного файла нет в архиве или текущих данных недостаточно для разрешения конкретного вопроса.

Не смешивай первоисточники и интерпретации: сохранённый оригинальный CSS и Styleguide находятся в `source/`, исследовательские выдержки — в `research/` и `source/reference-pages.md`, решения — в `decisions.md`, реестр отличий — в `changes.md`.

## Происхождение снимка

- Upstream: https://github.com/XXIIVV/oscean
- Ветка: `main`
- Upstream commit на момент сбора: `55083bb58ad6cdfb3a8e9ba3c91ba9645f5602d9`
- CSS blob SHA: `8e3ebd80245f0efa664d0178f14311c1bedaa4d8`
- Дата сбора: 2026-10-09

Это снимок, не автоматическое зеркало. При обновлении архива укажи новый upstream commit и дату.
