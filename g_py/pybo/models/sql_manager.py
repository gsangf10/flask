import pybo.models.db_util as db

def select_user():
    sql = "select * from USER"
    sql_list = db.get_list(sql)
    return sql_list

    
def insert_user(user_dic):
    sql = f'''
    INSERT INTO USER (LOGIN_ID, LOGIN_PW, USER_NAME, SEX, AGE, REG_DATE, MOD_DATE)
    VALUES ('{user_dic['login_id']}', '{user_dic['login_pw']}', '{user_dic['user_name']}', {user_dic['sex']}, {user_dic['age']}, NOW(), NOW())
    '''
    print(sql)
    db.set_data(sql)