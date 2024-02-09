from app.views.auth import bp
from flask import render_template, request, redirect, url_for
from app.views.auth import utils
from flask import flash
from app.models import db, cursor
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from flask_login import login_user

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if utils.login(username, password):
            return redirect(url_for('main.index'))
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    utils.logout()
    return redirect(url_for('main.index'))

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password2=request.form['password2']
        email=request.form['email']
        city=request.form['city']
        if utils.register(username, password, password2, city,email):
            return redirect(url_for('main.index'))

    return render_template('auth/signup.html')
