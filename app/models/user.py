from app.models import db, cursor
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, username, password, city, *args):
        self.id = id
        self.username = username
        self.password = password
        self.city = city

    def get_user_by_id(id):
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        return User(*result) if result else None
    
    def register_user(username, password_hash, city):
        query = "INSERT INTO users (username, password, city) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, password_hash, city))
        db.commit()

    def get_user_by_username(username):
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return User(*result) if result else None
    
    def update_user(current_username, username, city):
        query = "UPDATE users SET username = %s, city = %s WHERE username = %s"
        cursor.execute(query, (username, city, current_username))
        db.commit()
    