#import os
#import schedule
import smtplib
from email.message import EmailMessage



# Set up the email message
msg = EmailMessage()
msg['Subject'] = 'Test Email'
msg['From'] = 'intersum369@gmail.com'
msg['To'] = 'danieltarancon@gmail.com'
msg.set_content('This is a test email sent from Python.')

# Connect to the email server
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login('intersum369@gmail.com', 'password')

    # Send the email
    smtp.send_message(msg)


