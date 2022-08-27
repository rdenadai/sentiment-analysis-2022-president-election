from peewee import CharField, Model, TextField, TimestampField
from src.database.conn import db


class HashtagComments(Model):
    hash = CharField(primary_key=True, unique=True, index=True, max_length=255)
    hashtag = CharField(max_length=150, index=True)
    username = CharField(max_length=255)
    comment = TextField()
    data = CharField(max_length=50)
    timestamp = TimestampField(resolution=100)
    clean_comment = TextField(default="")
    sanitized_comment = TextField(default="")
    classify = CharField(max_length=50, default="", index=True)

    class Meta:
        database = db
        table_name = "hashtag_comments"
