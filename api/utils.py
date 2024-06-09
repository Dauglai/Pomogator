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

file_types = {
    "document": "https://docs.google.com/document/d/",
    "presentation": "https://docs.google.com/presentation/d/",
    "sheet": "https://docs.google.com/spreadsheets/d/",
    "folder": "application/vnd.google-apps.folder",
    "photo": "application/vnd.google-apps.photo",
    "forms": "https://docs.google.com/forms/d/"
}

SERVICE_ACCOUNT_FILE = 'credentials.json'

def create_google_file(name, data, type, id):
    #credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    credentials = get_credentials()
    event = Event.objects.get(id=id)
    service = build('drive', 'v3', credentials=credentials)
    fileId = ""
    if type == "document":
        fileId = create_google_doc(credentials, data, name)
    if type == "sheet":
        fileId = create_google_sheet(credentials, data, name)
    if type == "presentation":
        fileId = create_google_pres(credentials, data, name)
    if type == "forms":
        fileId = create_google_forms(credentials, data, name)
    if fileId == "":
        return fileId
    folder_id = make_document_public(service, fileId, event)
    new_doc = File(file_id=fileId, name=name, event=event, type=type, data=data, url=f'{file_types[type]}{fileId}', folder_id=folder_id)
    new_doc.save()
    return fileId


def create_google_doc(credentials, data, name):
    service = build('drive', 'v3', credentials=credentials)

    file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.document',
    }
    fh = BytesIO(data.encode())
    media = MediaIoBaseUpload(fh, mimetype='text/plain')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return file.get('id')

def create_google_sheet(credentials, data, name):
    service = build('sheets', 'v4', credentials=credentials)
    spreadsheet = service.spreadsheets().create(body={
        'properties': {'title': f'{name}', 'locale': 'ru_RU'},
        'sheets': [{'properties': {'sheetType': 'GRID',
                                   'sheetId': 0,
                                   'title': f'{data}',
                                   'gridProperties': {'rowCount': 100, 'columnCount': 15}}}]
    }).execute()
    return spreadsheet['spreadsheetId']


def create_google_pres(credentials, data, name):
    service = build('slides', 'v1', credentials=credentials)
    body = {"title": name}
    presentation = service.presentations().create(body=body).execute()
    return presentation.get('presentationId')

def create_google_forms(credentials, data, name):
    form_service = build("forms","v1", credentials=credentials)
    dict = {
        "info": {
            "title": name,
        },
    }
    form = form_service.forms().create(body=dict).execute()
    return form.get("formId")

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


def make_document_public(service, file_id, event):
    public_permission = {
        'type': 'anyone',
        'role': 'writer',
    }
    folder_id = get_folder_id(service, event)
    service.files().update(
            fileId=file_id,
            addParents=folder_id,
            removeParents="",
            fields="id, parents",
        ).execute()
    service.permissions().create(
        fileId=file_id,
        body=public_permission,
        fields='id',
    ).execute()
    return folder_id


def get_folder_id(service, event):
    service.files().list(
            q="mimeType='application/vnd.google-apps.folder'",
            spaces="drive",
            fields="nextPageToken, files(id, name)",
        ).execute()
    if event.file_set.count() == 0:
        metadata = {
            "name": event.title,
            "mimeType": "application/vnd.google-apps.folder",
        }
        folder = service.files().create(body=metadata, fields="id").execute()
        return folder.get("id")
    return File.objects.filter(event_id=event.id)[0].folder_id