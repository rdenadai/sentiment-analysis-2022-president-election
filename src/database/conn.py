import os

from playhouse.pool import PooledSqliteExtDatabase

db_name: str = "sentiment-analysis-2022-president-election.db"
path = os.getcwd().split("src")[0]

db = PooledSqliteExtDatabase(
    f"{path}/{db_name}",
    pragmas={
        "journal_mode": "wal",  # WAL-mode.
        "cache_size": -64 * 1000,  # 64MB cache.
        "foreign_keys": 1,
        "synchronous": 0,
    },
    max_connections=150,
    stale_timeout=3600,
    check_same_thread=False,
)
