from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'


def get_mail():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])

    if not messages:
        print("Brak wiadomości")
    else:
        temp = ""
        headers = ['Date', 'Subject']
        msg = service.users().messages().get(userId='me', id=messages[0]['id'], format='metadata', metadataHeaders = headers).execute()
        msg2 = service.users().messages().get(userId='me', id=messages[1]['id'], format='metadata', metadataHeaders= headers).execute()
        msg3 = service.users().messages().get(userId='me', id=messages[2]['id'], format='metadata',metadataHeaders= headers).execute()
        msg_headers = msg["payload"]["headers"]
        msg2_headers = msg2["payload"]["headers"]
        msg3_headers = msg3["payload"]["headers"]
        if len(msg_headers[1]['value']) > 25:
            msg_headers[1]['value'] = msg_headers[1]['value'][:25] + '...'
        if len(msg2_headers[1]['value']) > 25:
            msg2_headers[1]['value'] = msg2_headers[1]['value'][:25] + '...'
        if len(msg3_headers[1]['value']) > 25:
            msg3_headers[1]['value'] = msg3_headers[1]['value'][:25] + '...'
        date = datetime.datetime.strptime(msg_headers[0]['value'], '%a, %d %b %Y %H:%M:%S %z').\
            strftime('%d.%m.%Y %H:%M')
        date2 = datetime.datetime.strptime(msg2_headers[0]['value'], '%a, %d %b %Y %H:%M:%S %z').\
            strftime('%d.%m.%Y %H:%M')
        date3 = datetime.datetime.strptime(msg3_headers[0]['value'], '%a, %d %b %Y %H:%M:%S %z').\
            strftime('%d.%m.%Y %H:%M')
        response = "{} | {}\n" \
                   "{} | {}\n" \
                   "{} | {}     ".format(date, msg_headers[1]['value'],
                                         date2, msg2_headers[1]['value'],
                                         date3, msg3_headers[1]['value'])\
            .replace("<", "").replace(">", "")
        return response
