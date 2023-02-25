import smtplib
from email.message import EmailMessage
from key import password


recipients = ['intersum369@gmail.com', 'danieltarancon@gmail.com']

def auto_email(password):
    for recipient in recipients:
        # Set up the email message
        msg = EmailMessage()
        msg['Subject'] = 'Test Email'
        msg['From'] = 'danieltarancon@gmail.com'
        msg['To'] = recipient
        msg.set_content('This is a test email sent from Python.')

        # Connect to the Gmail SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()

            # Log in to the Gmail SMTP server with your email and password
            smtp.login('danieltarancon@gmail.com', password)

            # Send the email
            smtp.send_message(msg)

if __name__ == '__main__':
    auto_email(password)
