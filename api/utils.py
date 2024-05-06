from io import BytesIO

from google_auth_httplib2 import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
#from apiclient.http import MediaFileUpload
from api.models import File
import os.path
#from google.oauth2.service_account import Credentials
from google.oauth2.credentials import Credentials

from event.models import Event

#SCOPES = ["https://www.googleapis.com/auth/drive"]
SCOPES = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.metadata.readonly",
    "openid"
]
SERVICE_ACCOUNT_FILE = 'credentials.json'
file_types = {
    "document": "application/vnd.google-apps.document",
    "presentation": "application/vnd.google-apps.presentation",
    "sheet": "application/vnd.google-apps.spreadsheet",
    "folder": "application/vnd.google-apps.folder",
    "photo": "application/vnd.google-apps.photo"
}


def create_google_doc(name, data, type, event_id):
    #credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=get_credentials())
    mimetype = file_types[f"{type}"]
    file_metadata = {
        "name": f"{name}",
        "mimetype": mimetype
    }
    fh = BytesIO(data.encode())
    media = MediaIoBaseUpload(fh, mimetype='text/plain')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    id = file.get('id')
    make_document_public(service, id)
    event = Event.objects.get(id=event_id)
    new_doc = File(document_id=id, name=name, data=data, event=event, type=type)
    new_doc.save()
    return id


def get_credentials():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=8080)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


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