from app.models import db,cursor
from app.models.user import User
import requests
from flask_login import current_user

class Trade:
    def send_request(to, frm, book_id):
        cursor.execute("INSERT INTO requests (requested_id, requester_id, book_id1) VALUES (%s, %s, %s);", (to, frm, book_id))
        db.commit()
        cursor.execute("SELECT id FROM requests WHERE requested_id=%s and requester_id=%s and book_id1=%s;", (to, frm, book_id))
        request_id = cursor.fetchone()[0]
        cursor.fetchall()
        cursor.execute("INSERT INTO trade_status (request_id, stat) VALUES (%s, %s);", (request_id, "Pending"))
        db.commit()
    def confirm_trade(book1_id,book2_id,requester_name,requested_id):
        cursor.execute("SELECT id FROM users WHERE username=%s;",(requester_name,))
        requester_id = cursor.fetchone()[0]
        print("\n\n Requester ID: ",requester_id)
        print("\n\n Requested ID: ",requested_id)
        print("\n\n Book1 ID: ",book1_id[0])
        print("\n\n Book2 ID: ",book2_id[0])
        cursor.execute("UPDATE requests SET book_id2=%s WHERE requester_id=%s and requested_id=%s and book_id1=%s;",(book2_id[0],requester_id,requested_id,book1_id[0]))
        cursor.execute("SELECT id FROM requests WHERE requester_id=%s and requested_id=%s and book_id1=%s and book_id2=%s;",(requester_id,requested_id,book1_id[0],book2_id[0]))
        request_id = cursor.fetchone()[0]
        cursor.fetchall()
        cursor.execute("UPDATE trade_status SET stat=%s WHERE request_id=%s", ("Complete",request_id))
        db.commit()