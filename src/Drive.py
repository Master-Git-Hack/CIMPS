import pickle
from os import getenv
from os.path import exists

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from requests import get

from .config import Config


class Drive(Config):
    """class to handle the drive variables"""

    folder_id = getenv("DRIVE_FOLDER_ID", None)
    _scopes = [
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive.appdata",
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/drive.metadata",
        "https://www.googleapis.com/auth/drive.scripts",
    ]
    _access = None
    _service = None
    _id_file = None
    _current_file = None

    def __init__(self) -> None:
        if exists(self.paths.token):
            with open(self.paths.token, "rb") as _token:
                self._access = pickle.load(_token)
        if not self._access or not self._access.valid:
            self._access.refresh(Request())
        else:
            _flow = InstalledAppFlow.from_client_secrets_file(
                self.paths.credentials, self._scopes
            )
            self._access = _flow.run_local_server(port=0)
        with open(self.paths.token, "wb") as _token:
            pickle.dump(self._access, _token, protocol=2)

        self._service = build("drive", "v3", credentials=self._access)

    def upload(self, filename: str) -> bool or None:
        """function to upload a file to drive and convert it to pdf
        Args:
            filename (str): _description_
        Returns:
            bool or None: _description_
        """
        if self._service is None:
            self._service = build("drive", "v3", credentials=self._access)
        self._current_file = f"{self.paths.temp}/{filename}"

        body_metadata = dict(name=f"{filename}.pptx", parents=[self.folder_id])
        media = MediaFileUpload(
            f"{ self._current_file}.pptx",
            mimetype="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        )
        response = (
            self._service.files()
            .create(body=body_metadata, media_body=media, fields="id")
            .execute()
        )
        self.id_file = response.get("id")
        response = get(
            url=f"http://docs.google.com/presentation/d/{self.id_file}/export/pdf",
            allow_redirects=True,
        )
        with open(f"{ self._current_file}.pdf", "wb") as file:
            file.write(response.content)

        response = (
            self._service.files().delete(fileId=self.id_file, fields="id").execute()
        )
        if response:
            return self.id_file
        return None

    def protect(self, filename):
        """function to protect the pdf"""
        body_metadata = {"name": f"{filename}.pdf", "parents": [self.folder_id]}
        media = MediaFileUpload(
            f"{ self._current_file}.pdf", mimetype="application/pdf"
        )
        response = (
            self._service.files()
            .create(body=body_metadata, media_body=media, fields="id")
            .execute()
        )
        self._id_file = response.get("id")

        return (
            f"https://drive.google.com/uc?export=download&id={self._id_file}"
            if response
            else None
        )
