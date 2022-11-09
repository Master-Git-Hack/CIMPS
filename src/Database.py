from os import getenv
from os.path import join

from pymysql import connect, cursors

from .config import Config as _Config


class Database:
    """class to handle the database variables"""

    _host = getenv("DB_HOST", "localhost")
    _user = getenv("DB_USER", "root")
    _password = getenv("DB_PWD", None)
    _db = getenv("DB_NAME", None)
    _port = getenv("DB_PORT", "3306")
    sqlalchemy_database_uri = (
        f"mysql+pymysql://{_user}:{_password}@{_host}:{_port}/{_db}"
    )
    _paths = _Config().paths
    _schemas = dict(
        assistance="assistance.sql", workshop="workshop.sql", committe="committe.sql"
    )
    _current_schema = _schemas["assistance"]
    _cnxn = None

    def __init__(self, schema):
        try:
            self._cnxn = connect(
                host=self._host,
                port=int(self._port),
                user=self._user,
                password=self._password,
                database=self._db,
                cursorclass=cursors.DictCursor,
            )
        except (RuntimeError, TypeError, NameError):
            print(f"Error at sql services: {RuntimeError}")
            self._cnxn = False

        self._current_schema = join(self._paths.schemas, {self._schemas[schema]})

    def get(self) -> list:
        """function to get the data from the database
        Returns:
            list: list of dictionaries with the data
        """
        _query = open(self._current_schema).read()
        data = []
        if self._cnxn is not False:
            with self._cnxn.cursor() as _cursor:
                _cursor.execute(_query)
                rows = _cursor.fetchall()
                for row in rows:
                    data.append(
                        dict(
                            id_constancia=row["constancia"],
                            id_evento=row["id_evento"],
                            id_tipo_constancia=row["id_tipo_constancia"],
                            texto1=row["texto1"],
                            nombre=row["totexto2"],
                            texto3=row["texto3"],
                            genero=row["genero"],
                            cimps_ed=row["texto4"],
                            email=row["email"],
                        )
                    )
        return data

    def update(self, data: list, filename: str, url: str) -> None:
        """function to update the database with the certificates
        Args:
            data (list): list of dictionaries with the data to update
            filename (str): name of the file to update
            url (str): url of the file to update
        Returns:
            None
        """
        if self._cnxn is not False:
            with self._cnxn.cursor() as _cursor:
                _query = f"""
                UPDATE 
                    constancia 
                SET 
                    nombre_archivo='{filename}.pdf',
                    url='{url}',
                    generado=1 
                WHERE 
                    id={data['id_constancia']}
                    AND
                    id_tipo_constancia={data['id_tipo_constancia']}
            """
                _cursor.execute(_query)
                self._cnxn.commit()
