import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "kgmit18@gmail.com"
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

msg = EmailMessage()
msg['Subject'] = "Test email!"
msg['From'] = EMAIL_ADDRESS
msg['To'] = ['kgmit18@gmail.com']

msg.set_content('This is a test email!')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
