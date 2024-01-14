from flask import Blueprint

bp = Blueprint('user',__name__)

from app.views.user import routes
