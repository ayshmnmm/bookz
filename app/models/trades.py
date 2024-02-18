from app.models import db,cursor
from app.models.user import User
import requests
from flask_login import current_user

class Trade:
    def send_request(to,frm,book_id):
        cursor.execute("INSERT INTO requests (requested_id,requester_id,book_id1) VALUES(%s,%s,%s)",(frm,to,book_id))
        db.commit()