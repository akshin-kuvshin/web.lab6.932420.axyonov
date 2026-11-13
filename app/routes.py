from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return 'main page\n'

@bp.route('/about')
def about():
    return '\'about me\' page\n'
