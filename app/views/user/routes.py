from app.views.user import bp
from flask import render_template, request, redirect, url_for, flash
from app.views.user import utils
from flask_login import current_user, login_required


@bp.route('/user/<username>')
def profile(username):
    user = utils.get_user(username)
    if user:
        books = utils.library()
        return render_template('user/profile.html', books=books,user=user)
    else:
        flash('User not found')
        return render_template('404.html'), 404
    
@bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        username = request.form['username']
        city = request.form['city']
        if utils.update_user(username, city):
            return redirect(url_for('user.profile', username=username))
    return render_template('user/settings.html')

@bp.route('/lib/<use>')
@login_required
def user_library(use):
    books = utils.library(use)
    return render_template('user/library.html', books=books)

@bp.route('/library')
def library():
    books = utils.library()
    return render_template('user/library.html', books=books)