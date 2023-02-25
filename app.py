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
from key import api_key_file




# Set up the email message
msg = EmailMessage()
msg['Subject'] = 'Test Email'
msg['From'] = 'danieltarancon@gmail.com'
msg['To'] = 'intersum369@gmail.com'
msg.set_content('This is a test email sent from Python.')


# Connecting with the server
def authenticate_gmail_api(api_key_file):
    # Set up the OAuth 2.0 flow
    flow = InstalledAppFlow.from_client_secrets_file(
        api_key_file,
        scopes=['https://www.googleapis.com/auth/gmail.send']
    )
    credentials = flow.run_local_server(port=0)
    authed_session = google.auth.transport.requests.AuthorizedSession(credentials)
    service = build('gmail', 'v1', credentials=credentials)

    return service


service = authenticate_gmail_api(api_key_file)



# Call the Gmail API to send the message
def send_email(service, message):
    try:
        message = (service.users().messages().send(userId="me", body=message).execute())
        print(f"Message Id: {message['id']}")
    except HttpError as error:
        print(f"An error occurred: {error}")
        message = None
    return message

send_email(service, msg)




