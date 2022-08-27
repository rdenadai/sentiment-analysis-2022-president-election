from src.database.conn import db
from src.database.models import HashtagComments

if __name__ == "__main__":
    db.connect()
    db.create_tables(
        [
            HashtagComments,
        ]
    )
