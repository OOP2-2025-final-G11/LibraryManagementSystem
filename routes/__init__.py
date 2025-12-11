from .user import user_bp
from .product import product_bp
from .order import order_bp
from .book_request import book_request_bp

# Blueprintをリストとしてまとめる
blueprints = [
  user_bp,
  product_bp,
  order_bp,
  book_request_bp,
]
