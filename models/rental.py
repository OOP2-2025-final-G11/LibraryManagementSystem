from peewee import Model, ForeignKeyField, DateTimeField
from .db import db
from .user import User
from .book import Book


class Rental(Model):
    user = ForeignKeyField(User, backref='rental')
    book = ForeignKeyField(Book, backref='rental')
    rental_date = DateTimeField()
    return_date = DateTimeField(null=True)

    class Meta:
        database = db