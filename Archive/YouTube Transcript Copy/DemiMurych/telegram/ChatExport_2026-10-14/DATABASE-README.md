# SQLite: история группы As For JS - Talks

Файл `membership-history.sqlite3.sql` — одnofайловый SQL-дамп SQLite. Он создаёт локальную базу данных SQLite; это не бинарный файл базы.

## Создание файла базы

Из этого каталога запусти:

```powershell
sqlite3.exe membership-history.db ".read membership-history.sqlite3.sql"
```

Результат — один файл `membership-history.db`, который можно открывать SQLite Browser, Python sqlite3 или командной строкой sqlite3.

## Источники и состав

1. [Telegram Desktop HTML export, 10.05.2023–14.10.2026](https://github.com/devAItester/aishare/tree/main/Archive/YouTube%20Transcript%20Copy/DemiMurych/telegram/ChatExport_2026-10-14)
   - просканированы все 252 HTML-страницы;
   - извлечено 5 730 системных/service-событий;
   - 5 711 записей классифицированы как `invite`;
   - остальные — преобразование группы, смена названия/фото, закрепления и другие service-события;
   - в выгрузке не обнаружены отдельные записи типов join, leave, kick/remove или ban.
   - HTML service-сообщения не содержат точного времени; `date_hint` — дата предшествующего разделителя, `timestamp_utc` оставлен NULL.

2. [Telegram Desktop JSON export, 01.10.2026–21.11.2026](https://github.com/devAItester/menu/blob/main/share/result%20%282%29.json)
   - проиндексированы все 18 388 сообщений: Telegram message ID, Unix timestamp и sender ID;
   - добавлена таблица соответствия 109 sender ID и имён;
   - 285 сообщений с ключевыми словами сохранены отдельно как `message_context_candidates`. Это контекст для проверки, а не подтверждённые действия над участниками.

## Таблицы

- `service_events` — системные события из HTML.
- `messages_index` — индекс всех сообщений JSON-экспорта.
- `sender_names` — sender ID и отображаемые имена.
- `message_context_candidates` — текст сообщений-кандидатов для ручной проверки.
- `export_metadata` — источники, счётчики и параметры извлечения.

## Примеры запросов

```sql
-- Системные события по типам
SELECT event_type, COUNT(*)
FROM service_events
GROUP BY event_type
ORDER BY COUNT(*) DESC;

-- Все приглашения по датам
SELECT date_hint, COUNT(*)
FROM service_events
WHERE event_type = 'invite'
GROUP BY date_hint
ORDER BY date_hint;

-- Активность отправителей по дням (JSON-экспорт)
SELECT date(datetime(date_unix, 'unixepoch')) AS utc_day,
       sender_id, COUNT(*) AS messages
FROM messages_index
GROUP BY utc_day, sender_id
ORDER BY utc_day, messages DESC;

-- Сообщения-кандидаты для контекстной проверки
SELECT date_local, sender_name, message_text
FROM message_context_candidates
ORDER BY date_local;
```

## Ограничения интерпретации

Приглашение не тождественно подтверждённому вступлению. Обычный текст «я забанил» или «удалил» не является системным событием. Отсутствие join/leave/ban/remove в HTML-экспорте означает только, что таких service-записей нет в этой выгрузке; это не доказывает, что соответствующих действий не было. Для причинной атрибуции численности использовать Admin Log и снимки Telegram Statistics из репозитория `devAItester/tgadmlog`.
