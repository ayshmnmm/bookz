from flask_login import current_user, login_user, logout_user,current_user
from flask import flash
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

def login(username, password):
    user = User.get_user_by_username(username)
    if user is None:
        flash('Invalid username: does not exist', 'error')
        return False
    if not check_password_hash(user.password, password):
        flash('Invalid password', 'error')
        return False
    login_user(user)
    flash('Logged in successfully', 'success')
    return True
    
def register(username, password, password2, city,email):
    user = User.get_user_by_username(username)
    if user is not None:
        flash('Username already exists', 'error')
        return False
    elif password != password2:
        flash('Passwords do not match', 'error')
        return False
    elif len(password) < 5:
        flash('Password must be at least 5 characters', 'error')
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
    
    password_hash = generate_password_hash(password)
    User.register_user(username, password_hash, city,email)
   # login_user(User.get_user_by_username(username))
    flash('Registered successfully', 'success')
    return True

def logout():
    logout_user()
    flash('Logged out successfully', 'info')
    return True
