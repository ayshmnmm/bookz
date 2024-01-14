from app.models.user import User
from flask_login import current_user
from flask import flash

def get_user(username):
    return User.get_user_by_username(username)

def update_user(username, city):
    user = User.get_user_by_username(username)
    if user is not None and user.username != current_user.username:
        flash('Username already exists', 'error')
        return False
    elif len(username) < 3 or len(username) > 12:
        flash('Username must be between 3 and 12 characters', 'error')
        return False
    elif not username.isalnum():
        flash('Username must be alphanumeric', 'error')
        return False
    elif len(city) > 50:
        flash('City must be less than 50 characters', 'error')
        return False
    User.update_user(current_user.username, username, city)
    current_user.username = username
    current_user.city = city
    flash('Updated successfully', 'success')
    return True
