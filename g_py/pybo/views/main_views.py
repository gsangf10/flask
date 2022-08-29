from flask import Blueprint, render_template, request
import pybo.models.user_sql as sm

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/showForm')
def show_form():
    return render_template("form.html")


@bp.route('/')
def index():
    return render_template("main.html")
