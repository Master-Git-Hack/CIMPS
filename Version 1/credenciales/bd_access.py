import pymysql
#import paramiko
#from paramiko import SSHClient

#_host='10.102.1.65'
#_user='jmejia'
#_pwd='SFiAwwJEFjL7avaB'
_dbuser='root'
_dbpwd='#V0ngolaX'
_db='ingsofti_CIMPS3'


try:
#        ssh = SSHClient()
#        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#        ssh.connect(
#            hostname=_host,
#            username=_user,
#            password=_pwd
#        )
    #entrada, salida, error = ssh.exec_command('ls -la')
    #print(salida.read())
    cnxn = pymysql.connect(
        host = 'localhost',
        port = 3306,
        user = _dbuser,
        password = _dbpwd,
        db=_db)
except Exception as e:
    print("Error:", e)
    cnxn = False
#    finally:
#        if cnxn != False:
#            with cnxn.cursor() as cursor:
#                query = 'SELECT * FROM tipo_constancia'
#                cursor.execute(query)
#                datos = cursor.fetchall()
#                print(datos)

