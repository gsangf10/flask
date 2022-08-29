from flask import Blueprint, render_template, url_for, request, session
from werkzeug.utils import redirect
import pybo.models.user_sql as db

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
    
    db.insert_user(user_dic)
        
    return redirect(url_for('user.select_user', user_dic=user_dic))

        
@bp.route('/select_user')
def select_user():
    user_list = db.select_user()
    return render_template('user/user_list.html', user_list=user_list)


@bp.route('/login_form')
def login_form():
    return render_template('/login_form.html')


@bp.route('/login_check')
def login_check():
    login_id = request.args.get("login_id")
    login_pw = request.args.get("login_pw")
    
    target = db.get_user(login_id)
    
    if target == None:
        return "없는 회원입니다."

    if target['LOGIN_PW'] != login_pw:
        return "비밀번호가 다릅니다"
    
    session['login_user'] = target
    
    return redirect(url_for('main.index'))


@bp.route('/logout')
def logout():
    session.pop("login_user", None)
    return redirect(url_for('main.index'))