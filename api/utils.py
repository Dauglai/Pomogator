import httplib2
from google_auth_httplib2 import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from api.models import File
import os.path
from google.oauth2.credentials import Credentials
from event.models import Event
#from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from io import BytesIO
from oauth2client.service_account import ServiceAccountCredentials

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

def create_google_doc(data, name, id):
    #credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    credentials = get_credentials()
    service = build('drive', 'v3', credentials=credentials)

    file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.document'
    }
    fh = BytesIO(data.encode())
    media = MediaIoBaseUpload(fh, mimetype='text/plain')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    doc_id = file.get('id')
    make_document_public(service, doc_id)
    new_doc = File(document_id=doc_id, name=name, event=Event.objects.get(id=id), type="document")
    new_doc.save()

    return doc_id

def create_google_sheet(data, name, id):
    #credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    credentials = get_credentials()
    service = build('sheets', 'v4', credentials=credentials)

    spreadsheet = service.spreadsheets().create(body={
        'properties': {'title': f'{name}', 'locale': 'ru_RU'},
        'sheets': [{'properties': {'sheetType': 'GRID',
                                   'sheetId': 0,
                                   'title': f'{data}',
                                   'gridProperties': {'rowCount': 100, 'columnCount': 15}}}]
    }).execute()
    spreadsheetId = spreadsheet['spreadsheetId']
    servicev3 = build('drive', 'v3', credentials=credentials)
    make_document_public(servicev3, spreadsheetId)
    new_doc = File(document_id=spreadsheetId, name=name, event=Event.objects.get(id=id), type="sheet")
    new_doc.save()
    return spreadsheetId


def get_credentials():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            http = httplib2.Http()
            creds.refresh(Request(http))
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
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