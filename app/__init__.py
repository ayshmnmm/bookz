from flask import Flask, render_template
from config import Config
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        from app.models.user import User
        return User.get_user_by_id(user_id)

    from app.views.main import bp as main_bp
    from app.views.auth import bp as auth_bp
    from app.views.user import bp as user_bp
    from app.views.book import bp as book_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(book_bp, url_prefix='/book')

    return app
