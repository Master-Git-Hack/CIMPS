"""File to handle Email"""
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import getenv
from os.path import join
from smtplib import SMTP

from jinja2 import Template


class Email:
    """class to handle the email variables"""

    _email = "einar.serna@cimat.mx"  # getenv("EMAIL", None)
    _password = "#V0ngolaX_cimat"  # getenv("EMAIL_PASSWORD", None)
    _schema = "assistance"
    _message = None
    # delete
    current_edition = "11va"
    year = 22
    next_edition = "12va"
    next_year = 23
    ciudad_sede = "Monterrey"
    estado_sede = "Nuevo León"
    cimps_inicio = "19"
    cimps_termino = "21"
    public_password_for_file = 123

    def __init__(self, schema: str = None):
        self._message = MIMEMultipart()
        self._message["From"] = f"CIMPS<{self._email}>"
        self._message["Subject"] = f"CIMPS 20{self.year}: Constancia de Asistencia"
        if schema is not None:
            self._schema = schema

    def send(self, data: dict, to_email: str) -> bool:
        """
        Method to attach the files to the message
        Args:
            data (dict): data to render the template
            to_email (str): email of the participant
        Returns:
            bool: True if the email was sent
        """
        _template = Template(open(f"./src/templates/{self._schema}.html").read())
        _body = _template.render(
            TITLE=f"CIMPS 20{self.year}: Constancia de Asistencia",
            INTRO=data["Intro"],
            EDITION=self.current_edition,
            YEAR=self.year,
            NEXT_EDITION=self.next_edition,
            NEXT_YEAR=self.next_year,
            CIUDAD=self.ciudad_sede,
            ESTADO=self.estado_sede,
            INICIO=self.cimps_inicio,
            TERMINO=self.cimps_termino,
            PWD=self.public_password_for_file,
            LINK=data["Link"],
        )
        self._message.attach(MIMEText(_body, "html"))
        _file = open(f"./src/templates/commite.pptx", "rb")
        _mime = MIMEBase("application", "octet-stream")
        _mime.set_payload(_file.read())
        encoders.encode_base64(_mime)
        _mime.add_header("Content-Disposition", "attachment", filename=data["File"])
        self._message.attach(_mime)
        return self._send_email(self._message, to_email)

    def _send_email(self, message: MIMEMultipart, to_email: str) -> bool:
        """function to send email with the certificates

        Args:
            message (_type_): message with the files attached
            to_email (str): email of the participant

        Returns:
            bool: True if the email was sent
        """
        try:
            # Start server conecction
            _smtp_session = SMTP("smtp.gmail.com", 587)
            # Encryt the connection
            _smtp_session.starttls()

            # Sign In at server
            _smtp_session.login(self._email, self._password)

            # Send email
            _smtp_session.sendmail(self._email, to_email, message.as_string())

            # Finish server connection
            _smtp_session.quit()
            return True
        except (RuntimeError, TypeError, NameError):
            print(f"An error occurred at Email Service: {RuntimeError}")
            return False


_email = Email("committe")
_email.send(
    data=dict(Intro="Estimad@", Link="#", File="test.pptx"),
    to_email="e.serna.1a.43@gmail.com",
)
