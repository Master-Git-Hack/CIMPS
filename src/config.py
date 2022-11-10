"""File to handle configuration of the application."""
from datetime import date
from os import getcwd, getenv
from os.path import abspath, dirname, join

from dotenv import load_dotenv

load_dotenv()


class _Paths:
    """Class to store the paths of the project"""

    app_root = dirname(abspath(__file__))
    _templates = join(app_root, "templates")
    email_template = join(_templates, "message.html")
    schemas = join(app_root, "schemas")
    certificate_template = join(_templates, "certificate.pptx")
    temp = f"{getcwd()}/src/temp/"
    token = join(app_root, "token.pickle")
    credentials = join(app_root, "credentials.json")


class Config:
    """class to get the environment variables\
and set variables to use in the project
    """

    year = int(str(date.today().year).split("20")[1])
    next_year = year + 1
    current_edition = getenv("CIMPS_EDITION", f"20{year}")
    next_edition = getenv("CIMPS_NEXT_EDITION", f"20{next_year}")
    public_password_for_file = getenv(
        "PUBLIC_PASSWORD_FOR_FILE", f"CIMPS {current_edition}"
    )
    ciudad_sede = getenv("CIMPS_CIUDAD_SEDE", "Zacatecas")
    estado_sede = getenv("CIMPS_ESTADO_SEDE", "Zacatecas")
    cimps_inicio = getenv("CIMPS_INICIO", None)
    cimps_termino = getenv("CIMPS_TERMINO", None)
    paths = _Paths()
