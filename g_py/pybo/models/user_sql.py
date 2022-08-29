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
    db.set_data(sql)
    
    
def get_user(login_id):
    sql = f"SELECT * FROM USER WHERE LOGIN_ID='{login_id}'"
    return db.get_one(sql)