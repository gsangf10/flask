from flask import Blueprint, render_template, request
import pybo.models.sql_manager as sm

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/showForm')
def show_form():
    return render_template("form.html")


@bp.route('/')
def index():
    return render_template("main.html")


@bp.route('/get_article')
def get_article():
    a_list = sm.select_sql()
    return a_list