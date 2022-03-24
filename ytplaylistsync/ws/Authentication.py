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

    def authenticate(self) -> bool:
        if Config.resources['auth_token'].exists():
            self.__creds = Credentials.from_authorized_user_file(Config.resources['auth_token'], self.__scopes)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())