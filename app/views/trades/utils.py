import requests
from app.models import db,cursor
from app.models.trades import Trade

class Utils:
    def get_current_trades(user_id):
        cursor.execute("SELECT users.username,book_name FROM requests,users,book WHERE book_id1=book.book_id and requested_id=users.id and requester_id=%s",(user_id,))
        current_trades=cursor.fetchall()
        print("message sent")
        return current_trades