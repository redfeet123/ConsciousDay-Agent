import os
import sqlite3
from contextlib import contextmanager
from typing import Dict, List

DB_PATH = os.path.join(os.path.dirname(__file__), "entries.db")

@contextmanager
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                journal TEXT,
                intention TEXT,
                dream TEXT,
                priorities TEXT,
                reflection TEXT,
                strategy TEXT
            );
        """)
        conn.commit()

def insert_entry(entry: Dict) -> int:
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO entries (date, journal, intention, dream, priorities, reflection, strategy)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            entry["date"],
            entry["journal"],
            entry["intention"],
            entry["dream"],
            entry["priorities"],
            entry["reflection"],
            entry["strategy"],
        ))
        conn.commit()
        return cur.lastrowid

def get_dates() -> List[str]:
    with get_conn() as conn:
        return [row[0] for row in conn.execute("SELECT DISTINCT date FROM entries ORDER BY date DESC")]

def get_by_date(date: str) -> List[Dict]:
    with get_conn() as conn:
        rows = conn.execute("""
            SELECT * FROM entries WHERE date = ?
        """, (date,))
        keys = ["id", "date", "journal", "intention", "dream", "priorities", "reflection", "strategy"]
        return [dict(zip(keys, row)) for row in rows]
        
def delete_entry(entry_id: int):
    with get_conn() as conn:
        conn.execute("DELETE FROM entries WHERE id = ?", (entry_id,))
        conn.commit()

