from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from io import BytesIO
from api.models import GoogleDoc

SCOPES = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "https://www.googleapis.com/auth/drive",
    "openid"
]
SERVICE_ACCOUNT_FILE = 'client_secrets.json'

def create_google_doc(data, name):
    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)

    file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.document'
    }
    fh = BytesIO(data.encode())
    media = MediaIoBaseUpload(fh, mimetype='text/plain')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    make_document_public(service, file.get('id'))
    new_doc = GoogleDoc(document_id=file.get('id'), name=name)
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