from flask import Blueprint, render_template, request, redirect, url_for
from models import RequestBook, User
from datetime import datetime

request_book_bp = Blueprint('request_book', __name__, url_prefix='/request-books')


@request_book_bp.route('/')
def list():
    items = RequestBook.select()
    return render_template('request_book_list.html', title='新刊リクエスト一覧', items=items)


@request_book_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user_id = request.form['user_id']
        title = request.form['title']
        author = request.form['author']
        request_date = datetime.now()

        RequestBook.create(
            user=user_id,
            title=title,
            author=author,
            request_date=request_date
        )
        return redirect(url_for('request_book.list'))

    users = User.select()
    return render_template('request_book_add.html', users=users)


@request_book_bp.route('/edit/<int:request_id>', methods=['GET', 'POST'])
def edit(request_id):
    req = RequestBook.get_or_none(RequestBook.id == request_id)
    if not req:
        return redirect(url_for('request_book.list'))

    if request.method == 'POST':
        req.user = request.form['user_id']
        req.title = request.form['title']
        req.author = request.form['author']
        req.save()
        return redirect(url_for('request_book.list'))

    users = User.select()
    return render_template('request_book_edit.html', req=req, users=users)
