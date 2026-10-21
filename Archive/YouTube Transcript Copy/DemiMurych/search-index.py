#!/usr/bin/env python3
"""Build/search a local SQLite FTS5 index for DemiMurych YouTube transcripts.

Reads .vtt files without modifying them. The SQLite database is generated locally
and should not be committed; rebuild it after adding/updating transcripts.
"""
from __future__ import annotations

import argparse
import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "full"
DB = Path(__file__).resolve().parent / "transcripts.sqlite3"
TIMESTAMP = re.compile(r"(\d{2}:\d{2}:\d{2}\.\d{3})\s+-->\s+(\d{2}:\d{2}:\d{2}\.\d{3})")
TAG = re.compile(r"<[^>]+>")
SPACE = re.compile(r"\s+")


def parse_vtt(path: Path) -> tuple[str, list[tuple[str, str]]]:
    title = path.parent.name
    cues: list[tuple[str, str]] = []
    current_time = ""
    pending: list[str] = []
    for raw in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        line = raw.strip()
        match = TIMESTAMP.search(line)
        if match:
            if pending:
                text = SPACE.sub(" ", TAG.sub("", " ".join(pending))).strip()
                if text:
                    cues.append((current_time, text))
            current_time = match.group(1)
            pending = []
        elif not line or line.startswith(("WEBVTT", "Kind:", "Language:")):
            if pending:
                text = SPACE.sub(" ", TAG.sub("", " ".join(pending))).strip()
                if text:
                    cues.append((current_time, text))
                pending = []
        elif not re.fullmatch(r"\d+", line):
            pending.append(line)
    if pending:
        text = SPACE.sub(" ", TAG.sub("", " ".join(pending))).strip()
        if text:
            cues.append((current_time, text))
    return title, cues


def connect() -> sqlite3.Connection:
    con = sqlite3.connect(DB)
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("""CREATE VIRTUAL TABLE IF NOT EXISTS cues USING fts5(
        video UNINDEXED, path UNINDEXED, timestamp UNINDEXED, text,
        tokenize='unicode61 remove_diacritics 2'
    )""")
    con.execute("""CREATE TABLE IF NOT EXISTS files(
        path TEXT PRIMARY KEY, mtime_ns INTEGER NOT NULL, size INTEGER NOT NULL,
        video TEXT NOT NULL, cue_count INTEGER NOT NULL
    )""")
    return con


def build() -> None:
    if not ROOT.exists():
        raise SystemExit(f"Transcript directory not found: {ROOT}")
    con = connect()
    indexed = {row[0]: (row[1], row[2]) for row in con.execute("SELECT path, mtime_ns, size FROM files")}
    changed = removed = 0
    found = set()
    for path in sorted(ROOT.rglob("*.vtt")):
        rel = path.relative_to(ROOT).as_posix()
        stat = path.stat()
        found.add(rel)
        if indexed.get(rel) == (stat.st_mtime_ns, stat.st_size):
            continue
        title, cues = parse_vtt(path)
        con.execute("DELETE FROM cues WHERE path = ?", (rel,))
        con.executemany(
            "INSERT INTO cues(video,path,timestamp,text) VALUES(?,?,?,?)",
            [(title, rel, ts, text) for ts, text in cues],
        )
        con.execute(
            """INSERT INTO files(path,mtime_ns,size,video,cue_count) VALUES(?,?,?,?,?)
               ON CONFLICT(path) DO UPDATE SET mtime_ns=excluded.mtime_ns,
               size=excluded.size,video=excluded.video,cue_count=excluded.cue_count""",
            (rel, stat.st_mtime_ns, stat.st_size, title, len(cues)),
        )
        changed += 1
    stale = set(indexed) - found
    for rel in stale:
        con.execute("DELETE FROM cues WHERE path = ?", (rel,))
        con.execute("DELETE FROM files WHERE path = ?", (rel,))
        removed += 1
    con.commit()
    videos, cues = con.execute("SELECT COUNT(*), COALESCE(SUM(cue_count),0) FROM files").fetchone()
    con.close()
    print(f"Index: {DB}")
    print(f"Videos: {videos}; transcript segments: {cues}; updated: {changed}; removed: {removed}")


def search(query: str, limit: int) -> None:
    if not DB.exists():
        raise SystemExit(f"Index not found. Build it first: python {Path(__file__).name} build")
    con = sqlite3.connect(DB)
    try:
        rows = con.execute(
            """SELECT video,path,timestamp,snippet(cues,3,'[',']',' … ',18),bm25(cues)
               FROM cues WHERE cues MATCH ? ORDER BY bm25(cues) LIMIT ?""",
            (query, limit),
        ).fetchall()
    except sqlite3.OperationalError as exc:
        raise SystemExit(f"Search syntax error: {exc}\nUse quoted phrases or FTS5 terms, e.g. \"корпоративная этика\".") from exc
    if not rows:
        print("No matches. Try synonyms or broader terms.")
    for video, path, timestamp, snippet, _rank in rows:
        print(f"\n{video}\n  file: {path}\n  time: {timestamp or 'unknown'}\n  {snippet}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("build", help="create/update the local full-text index")
    find = sub.add_parser("search", help="search indexed transcript text")
    find.add_argument("query", help="FTS5 query; quote exact phrases")
    find.add_argument("-n", "--limit", type=int, default=20)
    args = parser.parse_args()
    if args.command == "build":
        build()
    else:
        search(args.query, max(1, args.limit))


if __name__ == "__main__":
    main()
