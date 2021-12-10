from src.config.google_services import service, MediaFileUpload
from src.config import drive_folder_id, temPath

def upload(filename):
    certificate = f'{temPath}{filename}'
    body_metadata = {
        'name': filename,
        'parents': [drive_folder_id]
    }
    print(certificate)
    media = MediaFileUpload(f'{certificate}', mimetype='application/pdf')

    response = service.files().create(
        body = body_metadata,
        media_body = media,
        fields='id'
    ).execute()


    return f'https://drive.google.com/uc?export=download&id={response.get("id")}' if response else None

