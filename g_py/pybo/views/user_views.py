from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect
import pybo.models.sql_manager as sm

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/insert_user_form')
def insert_user_form():
    return render_template('user/insert_user.html')

@bp.route('/insert_user')
def insert_user():
    
    login_id = request.args['login_id']
    login_pw = request.args['login_pw']
    user_name = request.args['user_name']
    sex = request.args['sex']
    age = request.args['age']
    
    user_dic = {}
    user_dic['login_id'] = login_id
    user_dic['login_pw'] = login_pw
    user_dic['user_name'] = user_name
    user_dic['sex'] = sex
    user_dic['age'] = age
    
    sm.insert_user(user_dic)
    
    flag = request.args.get('flag')
    
    return redirect(url_for('user.select_user', user_dic=user_dic, flag=flag))


@bp.route('/select_user')
def select_user():
    user_list = sm.select_user()
    print(user_list)
    return render_template('user/select_user.html', user_list=user_list)