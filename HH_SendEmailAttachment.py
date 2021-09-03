#Program to send an email attachment
import smtplib
import imghdr
from email.message import EmailMessage
import os

email_to = os.environ.get('EMAIL_TO')
email_from = os.environ.get('EMAIL_FROM')
email_psswd = os.environ.get('EMAIL_APP_PSSWD')
email_server = os.environ.get('EMAIL_SMTP_SERVER')
path_to_image = os.environ.get('PATH_TO_HH_SCREENSHOT_IMAGE')

msg = EmailMessage()
msg['Subject'] = 'Daily HH  Settlement - GCE'
msg['From'] = email_from
msg['To'] = email_to
msg.set_content('Screenshot attached...')

with open(path_to_image + '/HH_FirefoxScreenShot.png', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL(email_server, 465) as smtp:
    smtp.login(email_from, email_psswd)
    smtp.send_message(msg)
