from src.config.google_services import service, MediaFileUpload
from src.config import drive_folder_id, temPath
from requests import get
from src.utils.template_utils import protect_pdf

def upload(filename, email):
    certificate = f'{temPath}{filename}'
    body_metadata = {
        'name': f'{filename}.pptx',
        'parents': [drive_folder_id]
    }
    media = MediaFileUpload(f'{certificate}.pptx', mimetype='application/vnd.openxmlformats-officedocument.presentationml.presentation')
    response = service.files().create(
        body = body_metadata,
        media_body = media,
        fields='id'
    ).execute()
    file_Id = response.get("id")
    response = get(url = f'http://docs.google.com/presentation/d/{file_Id}/export/pdf', allow_redirects = True)
    with open(f'{certificate}.pdf', 'wb') as file:
        file.write(response.content)

    response = service.files().delete(fileId = file_Id, fields='id').execute()

    
    if protect_pdf(certificate, email):
        body_metadata = {
            'name': f'{filename}.pdf',
            'parents': [drive_folder_id]
        }
        media = MediaFileUpload(f'{certificate}.pdf', mimetype='application/pdf')
        response = service.files().create(
            body = body_metadata,
            media_body = media,
            fields='id'
        ).execute()
        file_Id = response.get("id")

    
        return f'https://drive.google.com/uc?export=download&id={file_Id}' if response else None
    else:
        return None