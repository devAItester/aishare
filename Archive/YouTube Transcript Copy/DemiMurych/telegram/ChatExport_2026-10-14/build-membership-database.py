#!/usr/bin/env python3
"""Build and verify membership-history.sqlite3 from its SQL import file."""

from pathlib import Path
import os
import sqlite3
import sys

ROOT = Path(__file__).resolve().parent
SQL_FILE = ROOT / "membership-history.sqlite3.sql"
DB_FILE = ROOT / "membership-history.sqlite3"
TEMP_FILE = ROOT / "membership-history.sqlite3.tmp"


def main() -> int:
    args = set(sys.argv[1:])
    if args - {"--force"}:
        raise SystemExit("Usage: python3 build-membership-database.py [--force]")

    force = "--force" in args
    if DB_FILE.exists() and not force:
        raise SystemExit(
            f"Refusing to overwrite {DB_FILE.name}; use --force to rebuild it."
        )
    if not SQL_FILE.is_file():
        raise SystemExit(f"SQL source not found: {SQL_FILE}")

    if TEMP_FILE.exists():
        TEMP_FILE.unlink()

    try:
        connection = sqlite3.connect(TEMP_FILE)
        try:
            connection.executescript(SQL_FILE.read_text(encoding="utf-8"))

            integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
            if integrity != "ok":
                raise RuntimeError(f"SQLite integrity_check failed: {integrity}")

            event_count = connection.execute(
                "SELECT COUNT(*) FROM service_events"
            ).fetchone()[0]
            page_count = connection.execute(
                "SELECT COUNT(*) FROM source_pages"
            ).fetchone()[0]
            page_event_count = connection.execute(
                "SELECT COALESCE(SUM(service_event_count), 0) FROM source_pages"
            ).fetchone()[0]
            expected_events = int(
                connection.execute(
                    "SELECT value FROM export_metadata "
                    "WHERE key = 'service_event_rows'"
                ).fetchone()[0]
            )
            expected_pages = int(
                connection.execute(
                    "SELECT value FROM export_metadata "
                    "WHERE key = 'source_pages_expected'"
                ).fetchone()[0]
            )

            if event_count != expected_events:
                raise RuntimeError(
                    f"Event count mismatch: {event_count} != {expected_events}"
                )
            if page_count != expected_pages:
                raise RuntimeError(
                    f"Source-page count mismatch: {page_count} != {expected_pages}"
                )
            if page_event_count != event_count:
                raise RuntimeError(
                    f"Page/event reconciliation failed: "
                    f"{page_event_count} != {event_count}"
                )
        finally:
            connection.close()

        os.replace(TEMP_FILE, DB_FILE)
    except Exception:
        if TEMP_FILE.exists():
            TEMP_FILE.unlink()
        raise

    print(
        f"OK: {DB_FILE.name}; events={event_count}; "
        f"source_pages={page_count}; integrity_check={integrity}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
