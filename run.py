from src.modules.certificates import create as create_certificate
from src.modules.email import request as send_email
from src.modules.drive import upload as upload2Drive
from src.modules.db_operations import update as update2DB, get as get2DB
from src.utils.template_utils import end_process

def main():
    data = get2DB('assistance')
    print(len(data))
    for row in data:
        filename = create_certificate(row)
        certificate_link = upload2Drive(filename,row['email'])
        if certificate_link != None:
            if send_email(data = {
                'File':f'{filename}.pdf',
                'Email':row['email'],
                'Link':certificate_link,
                'Intro': f"Estimad{'o' if row['genero'] == 'his' else 'a'} {row['nombre'].upper()} ",
            }):
                print(f'Done for: {row["id_constancia"]}')
                end_process(filename)
                
        else: print(f'Something went wrong with {row["id_constancia"]}')




def start():
    main(int(intput('What do you want to do?\n1. Create Certificate\n2. Send Email\n3. Upload to Google Drive\n4. Update DB\n5. Get DB\n')))

if __name__ == '__main__':
    main()
