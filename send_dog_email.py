import os
import smtplib
import requests
from email.message import EmailMessage

dog_info = requests.get('https://api.thedogapi.com/v1/images/search').json()[0]
dog_image_url = dog_info['url']

EMAIL_ADDRESS = "kgmit18@gmail.com"
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

msg = EmailMessage()
msg['Subject'] = "Dog of the day!"
msg['From'] = EMAIL_ADDRESS
msg['To'] = ['kgmit18@gmail.com']

msg.set_content(f'Here is your dog!\n{dog_image_url}')
msg.add_alternative(f'Here is your dog!<br/><img src="{dog_image_url}" width="300px">', subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
