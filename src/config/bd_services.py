import pymysql
from src.config import db_host, db_port, db_user, db_pwd, db_name

try:
    cnxn = pymysql.connect(host = db_host,
        port = int(db_port),
        user = db_user,
        password = db_pwd,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor)
except Exception as e:
    print(f'Error at sql services: {e}')
    cnxn = False