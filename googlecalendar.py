import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file google_token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def auth():
    creds = None
    # The file google_token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('google_token.pickle'):
        with open('google_token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            pass
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'google_credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('google_token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('calendar', 'v3', credentials=creds)


def clear(calendar):
    service = auth()

    page_token = None
    while True:
        events = service.events().list(calendarId=calendar, pageToken=page_token).execute()
        for event in events['items']:
            service.events().delete(calendarId=calendar, eventId=event['id']).execute()
        if not page_token:
            break


def create_event(fb_event, calendar):
    service = auth()

    event = {
        'summary': fb_event['name'],
        # 'location': '800 Howard St., San Francisco, CA 94103',
        'description': fb_event['description'],
        'start': {
            'dateTime': fb_event['start_time'],
        },
        'end': {
            'dateTime': fb_event['end_time'],
        },
    }

    response = service.events().insert(calendarId=calendar, body=event).execute()

    return response['status']
