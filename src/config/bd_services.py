from pymysql import connect
from src.config import db_host as host, db_port as port, db_user as user, db_pwd as password, db_name as db

try:
    cnxn = connect(host, port, user, password, db)
except Exception as e:
    print(f'Error at sql services: {e}')
    cnxn = False