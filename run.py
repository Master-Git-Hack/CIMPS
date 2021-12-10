from src.modules.certificates import create as create_certificate
from src.modules.email import request as send_email
from src.modules.drive import upload as upload2Drive
from src.modules.db_operations import update as update2DB, get as get2DB

def main():
    data = get2DB('assistance')
    for row in data:
        filename = create_certificate(row)
        certificate_link = upload2Drive(filename)
        if send_email(data = {
            'File':filename,
            'Email':'einar.serna@cimat.mx',
            'Link':certificate_link,
            'Intro': f"Estimad{'o' if row['genero'] == 'male' else 'a'} {row['nombre'].upper()} ",
        }):
            print(f'Done for: {row["id_constancia"]}')




def start():
    main(int(intput('What do you want to do?\n1. Create Certificate\n2. Send Email\n3. Upload to Google Drive\n4. Update DB\n5. Get DB\n')))

if __name__ == '__main__':
    main()
