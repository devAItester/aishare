# DemiMurych transcript search

A local full-text index for the transcript files in `full/`. The source transcripts are read-only; the generated SQLite database is local and is not committed to Git.

## Build or update

Run from the repository root:

```bash
python "Archive/YouTube Transcript Copy/DemiMurych/search-index.py" build
```

The indexer scans all `.vtt` files recursively. It updates only files whose size or modification time changed and removes stale entries. The database is written beside this document as `transcripts.sqlite3`.

## Search

```bash
python "Archive/YouTube Transcript Copy/DemiMurych/search-index.py" search '"корпоративная этика"'
python "Archive/YouTube Transcript Copy/DemiMurych/search-index.py" search 'улыбаются OR лицемерие OR вежливость' --limit 30
python "Archive/YouTube Transcript Copy/DemiMurych/search-index.py" search 'работают плохо'
```

Search uses SQLite FTS5 syntax. Results include the video title, transcript path, cue timestamp, and a text snippet. If an exact phrase has no results, try synonyms, alternate spellings, or a broader query.

## Notes

- Requires Python 3 and SQLite built with FTS5 (normally included in standard Python distributions).
- The timestamp points to the matching subtitle cue, not necessarily the beginning of the full discussion.
- Re-run `build` after syncing new or changed transcripts.
- The database is reproducible and should remain untracked; commit the script and these instructions, not the generated database.
