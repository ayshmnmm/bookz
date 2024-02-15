from app.views.trades import bp 
from flask import render_template
from app.models.book import Book
from app.models.trades import Trade
from app.views.trades.utils import Utils
from flask_login import current_user

@bp.route('/<to>/<book_id>')
def send_request(to,book_id):
    if to:
        Trade.send_request(to=to,frm=current_user.id,book_id=book_id)
        books=Book.recent_books()
        #current_trades=Utils.get_current_trades(current_user.id)
        return render_template('home/homepage.html',books=books)
    books=Book.recent_books()
    return render_template('home/homepage.html',books=books)