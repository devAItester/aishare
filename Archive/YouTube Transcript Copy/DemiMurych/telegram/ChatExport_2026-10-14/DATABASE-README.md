# SQLite: история группы As For JS - Talks

`membership-history.sqlite3.sql` — однофайловый SQL-дамп SQLite. Это SQL-скрипт, который создаёт локальный бинарный файл базы данных; сам файл в репозитории хранится в текстовом SQL-формате.

## Создание локальной базы

В этом каталоге выполни:

```powershell
sqlite3.exe membership-history.db ".read membership-history.sqlite3.sql"
```

Появится единый файл `membership-history.db`. Его можно открывать SQLite Browser, Python `sqlite3` или CLI `sqlite3`.

## Состав и источники

1. [Telegram Desktop HTML export, 10.05.2023–14.10.2026](https://github.com/devAItester/aishare/tree/main/Archive/YouTube%20Transcript%20Copy/DemiMurych/telegram/ChatExport_2026-10-14)
   - все 252 HTML-страницы отмечены как просканированные;
   - извлечено 4 498 системных/service-событий с 194 страниц;
   - типы: 4 481 invite, 4 group_title, 4 pin, 3 poll_action, 2 voice_chat, 2 group_boost, 1 group_conversion, 1 group_photo;
   - отдельные service-события join, leave, ban, kick или remove в экспорте не обнаружены;
   - точного времени в HTML service-блоках нет: `date_hint` — дата предыдущего разделителя, `timestamp_utc` остаётся NULL.

2. [Telegram Desktop JSON export, 01.10.2026–21.11.2026](https://github.com/devAItester/menu/blob/main/share/result%20%282%29.json)
   - проиндексированы все 18 388 сообщений: Telegram message ID, Unix timestamp и sender ID;
   - добавлена таблица соответствия 109 sender ID и отображаемых имён;
   - 285 сообщений, совпавших с поиском ключевых слов о банах, удалениях, вступлениях, выходах и администраторах, сохранены отдельно как контекстные кандидаты.

## Таблицы

- `export_metadata` — источники, диапазоны дат, счётчики и ограничения.
- `service_events` — системные события из HTML-экспорта.
- `messages_index` — индекс всех сообщений JSON-экспорта.
- `sender_names` — sender ID и отображаемые имена.
- `message_context_candidates` — текст 285 сообщений для ручной контекстной проверки.

## Примеры запросов

```sql
-- Системные события по типам
SELECT event_type, COUNT(*)
FROM service_events
GROUP BY event_type
ORDER BY COUNT(*) DESC;

-- Приглашения по датам
SELECT date_hint, COUNT(*) AS invites,
       MIN(telegram_message_id) AS first_message_id
FROM service_events
WHERE event_type = 'invite'
GROUP BY date_hint
ORDER BY first_message_id;

-- Активность отправителей по дням (UTC, JSON-экспорт)
SELECT date(datetime(m.date_unix, 'unixepoch')) AS utc_day,
       m.sender_id, s.sender_name, COUNT(*) AS messages
FROM messages_index AS m
LEFT JOIN sender_names AS s USING(sender_id)
GROUP BY utc_day, m.sender_id, s.sender_name
ORDER BY utc_day, messages DESC;

-- Контекстные сообщения, найденные по ключевым словам
SELECT date_local, sender_name, message_text
FROM message_context_candidates
ORDER BY date_local;
```

## Ограничения интерпретации

- Приглашение не тождественно подтверждённому вступлению.
- 285 контекстных сообщений — только результат поиска по ключевым словам; совпадение не означает, что описанное действие действительно произошло.
- Отсутствие join/leave/ban/kick/remove среди service-записей означает только, что таких записей нет в этой выгрузке.
- Для причинной атрибуции изменений численности использовать Admin Log и снимки Telegram Statistics из `devAItester/tgadmlog`.
