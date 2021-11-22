import smtplib
import os
from credenciales.bd_access import cnxn
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from src.config import email_name as from_Email, email_template as template, year, edition, next_edition, next_year, public_pwd_for_file 

def create_message(to_Email, name, genre, drive_link):
    message = MIMEMultipart()
    message['From'] = from_Email
    message['To'] = to_Email
    message['Subject'] = f'CIMPS 20{year}: Constancia de Asistencia'

    refer_as = 'Estimad'
    if genre == 'male':
        refer_as += 'o'
    else:
        refer_as += 'a'
    message_template = open(template).read().format(refer_as, name, edition, year, next_edition, next_year, public_pwd_for_file, drive_link)
    message.attach(MIMEText(message_template,'html'))

def content(user, path, url):
    to_Email = user['Email']
    filename = user['Nombre_Archivo']
    message = MIMEMultipart(MIMEText("""
    
    """))


#load information to generate document

def consulta(user, path ):

    if cnxn!=False:
        with cnxn.cursor() as cursor:
            query="""
SELECT DISTINCT c.id,u.email,u.name, u.gender, c.nombre_archivo,c.url FROM constancia c INNER JOIN users u ON c.id=u.id WHERE nombre_archivo!= '' and url != '';
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            data=[]
            for row in rows:
#SELECT o2, e.id_locacion, uc.email
                data.append({
                    'Id':row[0],
                    'Email':row[1],
                    'Nombre':row[2],
                    'Genero':row[3],
                    'Nombre_Archivo':row[4],
                    'Url':row[5]
                })
            return data

def send_email(user):
   # Iniciamos los parámetros del script
    remitente ='conferencecimps@cimat.mx'
    destinatario = user['Email']
    nombre_adjunto = user['Nombre_Archivo']
    ruta_adjunto = f'./archivos/{nombre_adjunto}'

    # Creamos el objeto mensaje
    mensaje = MIMEMultipart()
    
    # Establecemos los atributos del mensaje
    mensaje['From'] = f'CIMPS<{remitente}>'
    mensaje['To'] = destinatario
    mensaje['Subject'] = 'CIMPS 2020: Constancia de Asistencia'
    saludo='Estimad@'
    if user['Genero']=='male':
        saludo='Estimado'
    else:
        saludo='Estimada'
    # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
    mensaje.attach(MIMEText(f"""
    

    """, 'html'))
    
    # Abrimos el archivo que vamos a adjuntar
    
    archivo_adjunto = open(ruta_adjunto, 'rb')
    
    # Creamos un objeto MIME base
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    # Y le cargamos el archivo adjunto
    adjunto_MIME.set_payload((archivo_adjunto).read())
    # Codificamos el objeto en BASE64
    encoders.encode_base64(adjunto_MIME)
    # Agregamos una cabecera al objeto
    adjunto_MIME.add_header('Content-Disposition', 'attachment', filename=nombre_adjunto)
    # Y finalmente lo agregamos al mensaje
    mensaje.attach(adjunto_MIME)
    
    # Creamos la conexión con el servidor
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    
    # Ciframos la conexión
    sesion_smtp.starttls()

    # Iniciamos sesión en el servidor
    sesion_smtp.login(remitente,'C1mps2020#')

    # Convertimos el objeto mensaje a texto
    texto = mensaje.as_string()

    # Enviamos el mensaje
    sesion_smtp.sendmail(remitente, destinatario, texto)

    # Cerramos la conexión
    sesion_smtp.quit() 


def main():
    try:
        users = consulta()
        for user in users:
            send_email(user)
    except Exception as error:
        print("\nSomething fail, check!!!\n",error)
    finally:
        print("Done")
    

#entra cualquiera, con correo gmail
#en caso de que no llegue, la asignacion ponerle contrase;a temporal

if __name__ == "__main__": 
    main()