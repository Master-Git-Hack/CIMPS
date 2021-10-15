import smtplib
import os
from credenciales.bd_access import cnxn
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#load information to generate document

def consulta():
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
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<p>{saludo} {user['Nombre'].upper()}</p>
<p>Agradecemos su participación en la 9na Edición del CIMPS 2020.</p>
<p>Esperamos contar con su participación para la 10ma, edición del CIMPS 2021, que será llevada a cabo del 20-22 de Octubre del 2021 con sede en la Ciudad de Torreón Coahuila. Si la sindemia del COVID permite realizar actividades presenciales será anunciada a través de las páginas y redes sociales del CIMPS.</p>
<p>No olvide visitar las paginas oficiales: cimps.cimat.mx y facebook/cimps</p>
<p>Adjuntamos su constancia de asistencia, para poder visualizar la constancia y/o realizar una impresión de esta debera utilizar la siguiente contraseña: <strong>#CiMPS_2020</strong></p>
<p>Tambien puede descargar la constancia a través del siguiente <a href="{user['Url']}">enlace</a></p>
<p>Saludos</p>
<p>Comité CIMPS</p>
</body>
</html>    

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