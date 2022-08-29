from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect
import pybo.models.music_sql as db

bp = Blueprint('music', __name__, url_prefix='/music')


@bp.route('/music_list')
def music_list():
    music_list = db.get_music_list()
    return render_template('music/music_list.html', music_list=music_list)