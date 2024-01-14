from flask import Blueprint

bp = Blueprint('auth',__name__)

from app.views.auth import routes
