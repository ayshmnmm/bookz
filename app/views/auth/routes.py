from app.views.auth import bp
from flask import render_template, request, redirect, url_for
from app.views.auth import utils


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if utils.login(username, password):
            return redirect(url_for('main.index'))

    return render_template('auth/login.html')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']
        city = request.form['city']
        if utils.register(username, password, password2, city):
            return redirect(url_for('main.index'))

    return render_template('auth/register.html')


@bp.route('/logout')
def logout():
    utils.logout()
    return redirect(url_for('main.index'))
