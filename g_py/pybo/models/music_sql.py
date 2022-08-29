import pybo.models.db_util as db

def get_music_list():
    sql = "select * from MUSIC"
    sql_list = db.get_list(sql)
    return sql_list
