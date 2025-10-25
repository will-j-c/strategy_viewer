from flask import Blueprint

bp = Blueprint('pairs', __name__)

from api.pairs import pairs