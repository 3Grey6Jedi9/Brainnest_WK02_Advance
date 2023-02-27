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
#from key import useful_data
import base64
import time, datetime
import numpy as np
import logging

#Setting up logging to a file
logging.basicConfig(filename='email_log.txt', level=logging.INFO, format='%(asctime)s %(message)s')


recipients = []

current_day = datetime.datetime.now().day

list_files = os.listdir(path='/Users/danielmulatarancon/Desktop/Documents/HACKING TIME/Brainnest /Week 02/Advance Tasks/Brainnest_WK02_Advance/super_month')

del list_files[0]

todays_file = ''


def file_day_assign(current_day, list_files):

    group_A = np.array([1,8,15,22,29])
    group_B = group_A + 1
    group_C = group_B + 1
    group_D = np.delete(group_C,4) + 1
    group_E = group_D + 1
    group_F = group_E + 1
    group_G = group_F + 1


    if current_day in group_A:
        todays_file = list_files[0]
    elif current_day in group_B:
        todays_file = list_files[1]
    elif current_day in group_C:
        todays_file = list_files[2]
    elif current_day in group_D:
        todays_file = list_files[3]
    elif current_day in group_E:
        todays_file = list_files[4]
    elif current_day in group_F:
        todays_file = list_files[5]
    elif current_day in group_G:
        todays_file = list_files[6]

    return todays_file






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




# Call the Gmail API to send the message
def send_email(service, message):
    try:
        message = (service.users().messages().send(userId="me", body=message).execute())
        print(f"Message Id: {message['id']}")
    except HttpError as error:
        print(f"An error occurred: {error}")
        message = None
    return message




def auto_email(useful_data):

    service = authenticate_gmail_api(useful_data)

    todays_file = file_day_assign(current_day, list_files)

    for recipient in recipients:
        msg = EmailMessage()
        msg['Subject'] = 'Super Month'
        msg['From'] = "User's email"
        msg['To'] = recipient
        msg.set_content('Let us conquer this day')


        file_path = os.path.join(
            '/Users/danielmulatarancon/Desktop/Documents/HACKING TIME/Brainnest /Week 02/Advance Tasks/super_month',
            todays_file)
        with open(file_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(file_path)

        msg.add_attachment(file_data, maintype='application', subtype='jpeg')

        # Converting the EmailMessage to a format compatible with the Gmail API
        mime_msg = msg.as_string().encode("utf-8")
        b64_msg = base64.urlsafe_b64encode(mime_msg).decode("utf-8")
        raw_msg = {"raw": b64_msg}

        send_email(service, raw_msg)

        logging.info(f"{datetime.datetime.now()} - email sent to {recipient}")



if __name__ == '__main__':
    set_up = ''
    instructions = '''\n     1) You must get a client secret ID OAth 2.0.\n
     2) Then having downloaded the json file, create a file called key.py. In that file you will import json and you
     will put that data into a variable (secret_data = json.load(f)).
     Eventually you will get the data requested, in this case --> useful_data = secrect_data['installed'].\n
     3) Indicate the inside the list recipients the emails that will receive the data.\n
     4) Now you will be able to run succesfully the app.\n
     5) Before I forget, once you run the app you will need to grant permission to run it since this app in the testing phase.\n'''
    print(instructions)
    while set_up != 'y' or ValueError:
        try:
            set_up = input('Did you set up the app [enter "y" for yes or "n" for no]? ').lower()
            if set_up != 'y' and set_up != 'n':
                raise ValueError('You must enter "y" or "n", try again please')
        except ValueError as err:
            print(f'{err}')
        else:
            if set_up == 'y':
                schedule.every().day.at("22:12").do(lambda: auto_email(useful_data))

                while True:
                    schedule.run_pending()
                    time.sleep(1)
            else:
                print(instructions)
                continue














