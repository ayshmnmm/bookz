from flask import Blueprint

bp = Blueprint('trade',__name__)

from app.views.trades import routes