import functools

from flask import Blueprint, request, render_template

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return render_template('index.html')
