import pickle
from os.path import dirname, join, abspath, exists
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import errors
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

SCOPES = ["https://www.googleapis.com/auth/drive.file",
          "https://www.googleapis.com/auth/drive.appdata",
          "https://www.googleapis.com/auth/drive",
          "https://www.googleapis.com/auth/drive.metadata",
          "https://www.googleapis.com/auth/drive.scripts"]

creds = None

app_root = dirname(abspath(__file__))
app_token = join(app_root, "token.pickle")
app_credentials = join(app_root,'credenciales.json')


if exists(app_token):
    with open(app_token, "rb") as token:
        creds = pickle.load(token)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            app_credentials, SCOPES)
        creds = flow.run_local_server(port=0)

    with open(app_token, "wb") as token:
        pickle.dump(creds, token, protocol=2)

service = build("drive", "v3", credentials=creds)