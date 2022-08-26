import pymysql as pysql
import pybo.config.db_info as db_conf

host = db_conf.host
user = db_conf.user
password = db_conf.password
database = db_conf.database


# 커넥션 얻어오기
def get_connection():
    conn = pysql.connect(host=host, user=user, password=password, database=database)
    return conn

# 커서 실행
def get_cursor(conn, sql):
    cur = conn.cursor(pysql.cursors.DictCursor)
    cur.execute(sql)
    return cur

# 결과 한개
def get_one(sql):
    conn = get_connection()
    cur = get_cursor(conn, sql)
    rs = cur.fetchone()  # 결과 중 맨 위 1개 -> 딕셔너리
    return rs
    
# 전체 결과
def get_list(sql):
    conn = get_connection()
    cur = get_cursor(conn, sql)
    rs = cur.fetchall()  # 결과 전체 -> 딕셔너리 리스트
    return rs

# 결과 변경
def set_data(sql):
    conn = get_connection()
    get_cursor(conn, sql)
    conn.commit()