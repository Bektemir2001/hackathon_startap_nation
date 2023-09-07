from flask import Blueprint

from api.v1 import search

bp = Blueprint('routes', __name__)

bp.register_blueprint(search.bp, url_prefix='/search')