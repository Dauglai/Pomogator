from io import BytesIO

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from api.models import GoogleDoc
import os.path
from google.oauth2.service_account import Credentials


SCOPES = ["https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = 'credentials.json'

def create_google_doc(name, data):
    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)

    file_metadata = {
        "name": f"{name}",
        "mimeType": "application/vnd.google-apps.document"
    }
    fh = BytesIO(data.encode())
    media = MediaIoBaseUpload(fh, mimetype='text/plain')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    make_document_public(service, file.get('id'))
    new_doc = GoogleDoc(document_id=file.get('id'), name=name, data=data)
    new_doc.save()
    return file.get('id')


def make_document_public(service, file_id):
    public_permission = {
        'type': 'anyone',
        'role': 'writer',
    }
    service.permissions().create(
        fileId=file_id,
        body=public_permission,
        fields='id',
    ).execute()