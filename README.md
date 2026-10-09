# Полевые заметки

Небольшой связанный сайт о проектировании текстовой базы знаний и исследовании референса [Oscean](https://github.com/XXIIVV/oscean).

- [Главная](index.html)
- [Проект](project.html)
- [Архитектура](architecture.html)
- [Навигация и связи](navigation.html)
- [Визуальный язык](styling.html)
- [Проверки публикации](publishing.html)
- [Реестр решений](decisions.html)
- [Источники](sources.html)
- [Карта сайта](map.html)

## Структура

- Корневые Markdown-файлы — содержимое страниц и локальные метаданные.
- _data/navigation.yml — данные основного меню.
- _layouts/default.html — общая HTML-оболочка.
- assets/main.css — оформление.
- Archive/ — временное хранилище исходных материалов в корне репозитория; сайт от него не зависит.

## Публикация

Сайт использует Jekyll и может публиковаться через GitHub Pages. Включи Pages в **Settings → Pages → Deploy from a branch → main → /(root)**. В _config.yml каталог Archive исключён из результата сборки.

Исходники проверены через GitHub API. Браузерная проверка и проверка опубликованной версии не выполнены; их нужно провести после включения Pages.
