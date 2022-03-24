import Config
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class Authentication:

    def __init__(self):
        self.__scopes = ['https://www.googleapis.com/auth/drive.metadata.readonly'] #TODO define the scope
        self.__creds = None

    def authenticate(self) -> Credentials:
        if Config.resources['auth_token'].exists():
            self.__creds = Credentials.from_authorized_user_file(Config.resources['auth_token'], self.__scopes)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(Config.resources['credentials'], self.__scopes)
                creds = flow.run_local_server(port=0)
            with open(Config.resources['auth_token'], 'w') as token:
                token.write(creds.to_json())
        
        return creds

    def commWithApi(self, creds:Credentials): #TODO
        try:
            service = build('drive', 'v3', credentials=creds)

            results = service.files.list(pageSize=10, fields="nextPageToken, files(id,name)").execute()
            items = results.get('files', [])

            if not items:
                print('No files found.')
                return
            print('Files:')
            for item in items:
                print(f'{item["name"]} ({item["id"]})')
        except HttpError as error:
            print(f'An error occured while authenticating: {error}')