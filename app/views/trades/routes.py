from app.views.trades import bp 
from flask import render_template
from app.models.book import Book
from app.models.trades import Trade
from app.views.trades.utils import Utils
from flask_login import current_user
from flask import request
@bp.route('/<to>/<book_id>')
def send_request(to,book_id):
    if to:
        Trade.send_request(to=to,frm=current_user.id,book_id=book_id)
        books=Book.recent_books()
        #current_trades=Utils.get_current_trades(current_user.id)
        return render_template('home/homepage.html',books=books)
    books=Book.recent_books()
    return render_template('home/homepage.html',books=books)

@bp.route('/trade')
def your_trade():
    trades=Utils.get_current_trades(current_user.id)
    return render_template('user/trade.html',trades=trades)

@bp.route('/trades/<book2_name>/<requester_name>', methods=['POST', 'GET'])
def confirm_trade(book2_name, requester_name):
    if request.method == 'POST':
        requested_id = current_user.id
        book1_name = request.form['selectedBook']
        book2_id=Book.get_by_name(book2_name)
        book1_id=Book.get_by_name(book1_name)
        Trade.confirm_trade(book1_id, book2_id, requester_name, requested_id)
        trades = Utils.get_current_trades(current_user.id)
        print("\n\n Last Step of confirm trade \n\n")
        return render_template('user/trade.html', trades=trades)