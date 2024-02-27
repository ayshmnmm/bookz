import requests
from app.models import db,cursor
from app.models.trades import Trade

class Utils:
    def get_current_trades(user_id):
        cursor.execute("SELECT users.id, users.username, book_name, stat FROM requests, users, book, trade_status WHERE requests.id = trade_status.request_id AND book_id1 = book.book_id AND requested_id = users.id AND requests.requester_id = %s", (user_id,))
        current_trades = cursor.fetchall()

        for i, trade in enumerate(current_trades):
            cursor.execute("SELECT book_name FROM book, library WHERE library.user_id = %s and library.book_id = book.book_id", (trade[0],))
            additional_books = cursor.fetchall()
            current_trades[i] = trade + (additional_books,)
        print("\n\n Current Trades: ",current_trades)
        return current_trades
