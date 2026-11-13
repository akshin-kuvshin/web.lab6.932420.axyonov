from flask import Blueprint, send_from_directory
from pathlib import Path

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return send_from_directory(
        Path(__file__).parent / 'static',
        'index.html'
    )

@bp.route('/about')
def about():
    return send_from_directory(
        Path(__file__).parent / 'static',
        'about.html'
    )
