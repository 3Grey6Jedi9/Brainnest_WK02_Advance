import os
import schedule
from email.message import EmailMessage
import google
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import google.auth
import google.auth.transport.requests
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from key import useful_data
import base64




# Set up the email message
msg = EmailMessage()
msg['Subject'] = 'Test Email'
msg['From'] = 'danieltarancon@gmail.com'
msg['To'] = 'intersum369@gmail.com'
msg.set_content('This is a test email sent from Python.')


# Converting the EmailMessage to a format compatible with the Gmail API
mime_msg = msg.as_string().encode("utf-8")
b64_msg = base64.urlsafe_b64encode(mime_msg).decode("utf-8")
raw_msg = {"raw": b64_msg}


# Connecting with the server
def authenticate_gmail_api(useful_data):
    # Set up the OAuth 2.0 flow
    flow = InstalledAppFlow.from_client_config(
        {
            "web": {
                "client_id": useful_data['client_id'],
                "project_id": useful_data['project_id'],
                "auth_uri": useful_data['auth_uri'],
                "token_uri": useful_data['token_uri'],
                "auth_provider_x509_cert_url": useful_data['auth_provider_x509_cert_url'],
                "client_secret": useful_data['client_secret'],
                "redirect_uris": useful_data['redirect_uris'],
                "javascript_origins": [],
            }
        },
        scopes=['https://www.googleapis.com/auth/gmail.send']
    )
    credentials = flow.run_local_server(port=0)
    authed_session = google.auth.transport.requests.AuthorizedSession(credentials)
    service = build('gmail', 'v1', credentials=credentials)

    return service


service = authenticate_gmail_api(useful_data)




# Call the Gmail API to send the message
def send_email(service, message):
    try:
        message = (service.users().messages().send(userId="me", body=message).execute())
        print(f"Message Id: {message['id']}")
    except HttpError as error:
        print(f"An error occurred: {error}")
        message = None
    return message

send_email(service, raw_msg)




