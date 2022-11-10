from src.modules.certificates import create as create_certificate
from src.modules.db_operations import get_workshops
from src.modules.db_operations import update as update2DB
from src.modules.drive import upload as upload2Drive
from src.modules.email import request as send_email
from src.utils.template_utils import end_process, getXLSXinfo


def main():
    data = getXLSXinfo()
    # data = get_workshos()

    row = data.to_dict("list")
    nombre = row["NOMBRE"]
    email = row["EMAIL"]
    for idx in range(len(nombre)):
        row = dict(
            nombre=nombre[idx],
            email=email[idx],
            title="TEST",
            year=22,
            id_constancia=idx,
            genero="male",
            titulo="TEST",
        )
        filename = create_certificate(row)
        certificate_link = upload2Drive(filename, row["email"])
        if certificate_link != None:
            if send_email(
                data={
                    "File": f"{filename}.pdf",
                    "Email": "einar.serna@gmail.com",
                    "Link": certificate_link,
                    "Intro": f"Estimad{'o' if row['genero'] == 'male' else 'a'} {row['nombre'].upper()} ",
                    "Taller": row["titulo"],
                }
            ):
                print(f'Done for: {row["id_constancia"]}')
                end_process(filename)
                break

        else:
            print(f'Something went wrong with {row["id_constancia"]}')


def start():
    main(
        int(
            intput(
                "What do you want to do?\n1. Create Certificate\n2. Send Email\n3. Upload to Google Drive\n4. Update DB\n5. Get DB\n"
            )
        )
    )


if __name__ == "__main__":
    main()
