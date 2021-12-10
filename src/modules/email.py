from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from jinja2 import Template

from src.config import email_name as from_Email, email_template as template, year, edition, next_edition, next_year, public_pwd_for_file, temPath

from src.config.email_services import send_email

def create_message(data):
    message = MIMEMultipart()
    message['From'] = f'CIMPS<{from_Email}>'
    message['To'] = data['Email']
    message['Subject'] = f'CIMPS 20{year}: Constancia de Asistencia'

    
    message_template = Template(open(template).read())
    
    message.attach(
        MIMEText(f"""
            {message_template.render(
                INTRO = data['Intro'],
                EDITION = edition,
                YEAR = year, 
                NEXT_EDITION = next_edition, 
                NEXT_YEAR = next_year, 
                PWD = public_pwd_for_file,
                LINK = data['Link']
            )}""",
        'html')
    )
    message.attach(attach_file(data['File']))
    return message

def attach_file(filename):
    file2attach = open(f'{temPath}{filename}', 'rb')
    mime2attach = MIMEBase('application', 'octet-stream')
    mime2attach.set_payload((file2attach).read())
    encoders.encode_base64(mime2attach)
    mime2attach.add_header('Content-Disposition', 'attachment', filename=filename)
    return mime2attach


def request(data):
    message = create_message(data)
    return send_email(message,to_Email=data['Email'])
