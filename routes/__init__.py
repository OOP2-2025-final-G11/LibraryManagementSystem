from .user import user_bp
from .product import product_bp
from .order import order_bp
from .request_book import request_book_bp

# Blueprintをリストとしてまとめる
blueprints = [
  user_bp,
  product_bp,
  order_bp,
  request_book_bp,
]
