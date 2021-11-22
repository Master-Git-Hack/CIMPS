from src.config.google_services import service, MediaFileUpload
from src.config import drive_folder_id, temPath

def upload_file(filename):
    filename = f'{filename}.pdf'
    body = {
        'name': filename,
        'parents': [drive_folder_id]
    }

    media_body = MediaFileUpload(f'{temPath}{filename}', mimetype='application/pdf')

    response = service.files().create(
        body,
        media_body,
        fields='id'
    ).execute()

    if response:
        return f'https://drive.google.com/uc?export=download&id={response.get("id")}'
    else: return None
