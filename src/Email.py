"""File to handle Email"""
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import getenv
from os.path import join
from smtplib import SMTP

from jinja2 import Template

from .config import Config


class Email(Config):
    """class to handle the email variables"""

    _email = getenv("EMAIL", None)
    _password = getenv("PASSWORD", None)
    _message = None

    def __init__(self):
        self._message = MIMEMultipart()
        self._message["From"] = f"CIMPS<{self._email}>"
        self._message["Subject"] = f"CIMPS 20{self.year}: Constancia de Asistencia"

    def send(self, data: dict, to_email: str) -> bool:
        """
        Method to attach the files to the message
        Args:
            data (dict): data to render the template
            to_email (str): email of the participant
        Returns:
            bool: True if the email was sent
        """
        _template = Template(open(self.paths.email_template).read())
        self._message.attach(
            MIMEText(
                f"""{_template.render(
                INTRO = data['Intro'],
                EDITION = self.current_edition,
                YEAR = self.year,
                NEXT_EDITION = self.next_edition,
                NEXT_YEAR = self.next_year,
                CIUDAD = self.ciudad_sede,
                ESTADO = self.estado_sede,
                INICIO=self.cimps_inicio,
                TERMINO=self.cimps_termino,
                PWD = self.public_password_for_file,
                LINK = data['Link']
        )}"""
            )
        )
        _file = open(join(self.paths.temp, data["File"]), "rb")
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
