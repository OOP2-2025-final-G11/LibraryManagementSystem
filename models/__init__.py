from peewee import SqliteDatabase
from .db import db
from .user import User
from .product import Product
from .order import Order
from .book_request import BookRequest

# モデルのリストを定義しておくと、後でまとめて登録しやすくなります
MODELS = [
    User,
    Product,
    Order,
    BookRequest,
]

# データベースの初期化関数
def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()