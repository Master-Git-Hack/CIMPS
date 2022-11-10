from .Certificates import Certificates
from .Database import Database
from .Drive import Drive
from .Email import Email


def main(schema: str = "assistance") -> None:
    """Main function to run the program"""
    #db = Database(schema=schema)
    #data = db.get()
    data = get_xlxs_info("Becas.xlsx", "Hoja 1")
    print(len(data))
    cert = Certificates()
    drive = Drive()
    email = Email()
    for row in data:
        _filename = cert.create(row)
        _to_email = row["email"]
        _link = drive.upload(_filename, _to_email)
        if _link is not None:
            if email.send(
                data=dict(
                    File=f"{_filename}.pdf",
                    Email=_to_email,
                    Link=_link,
                    Intro=f"Estimad{'o' if row['genero'] == 'his' else 'a'} {row['nombre'].upper()} ",
                ),
                to_email=_to_email,
            ):
                print(f"Done for: {row['id_constancia']}")
                cert.end_process(_filename)
