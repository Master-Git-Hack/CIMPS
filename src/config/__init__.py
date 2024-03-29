from dotenv import load_dotenv
from os import getenv, getcwd
load_dotenv()

#Templates paths
email_template = f'{getcwd()}/src/templates/message.html'
certificate_template = f'{getcwd()}/src/templates/certificate.pptx'
temPath = f'{getcwd()}/src/temp/'

# Google Drive paths

if getenv('DRIVE_FOLDER_ID'):
    drive_folder_id = getenv('DRIVE_FOLDER_ID')
else:
    print('No drive folder id for API found.')

# EMAIL information
if getenv('EMAIL_NAME'):
    email_name = getenv('EMAIL_NAME')
else:
    print('No Email element found')

if getenv('EMAIL_PWD'):
    email_pwd = getenv('EMAIL_PWD')
else:
    print('No Email element found')


#DB information
if getenv('DB_USER'):
    db_user = getenv('DB_USER')
else:
    print('No DB element found')

if getenv('DB_PWD'):
    db_pwd = getenv('DB_PWD')
else:
    print('No DB element found')

if getenv('DB_PORT'):
    db_port = getenv('DB_PORT')
else:
    print('No DB element found')

if getenv('DB_HOST'):
    db_host = getenv('DB_HOST')
else:
    print('No DB element found')

if getenv('DB_NAME'):
    db_name = getenv('DB_NAME')
else:
    print('No DB element found')


#CIMPS information
if getenv('CIMPS_YEAR'):
    year = int(getenv('CIMPS_YEAR'))
    next_year = year+1
else:
    print('No year information found')

if getenv('CIMPS_EDITION'):
    edition = getenv('CIMPS_EDITION')
else:
    print('No edition information found')

if getenv('CIMPS_NEXT_EDITION'):
    next_edition = getenv('CIMPS_NEXT_EDITION')
else:
    print('No next edition information found')

if getenv('PWD_FILE'):
    public_pwd_for_file = getenv('PWD_FILE')
else:
    print('No PWD FILE information found')

if getenv('CIMPS_CIUDAD_SEDE'):
    ciudad_sede = getenv('CIMPS_CIUDAD_SEDE')
else:
    print('No ciudad sede information found')

if getenv('CIMPS_ESTADO_SEDE'):
    estado_sede = getenv('CIMPS_ESTADO_SEDE')
else:
    print('No estado sede information found')

if getenv('CIMPS_INICIO'):
    cimps_inicio = getenv('CIMPS_INICIO')
else:
    print('No cimps inicio information found')

if getenv('CIMPS_TERMINO'):
    cimps_termino = getenv('CIMPS_TERMINO')
else:  
    print('No cimps termino information found')
    

