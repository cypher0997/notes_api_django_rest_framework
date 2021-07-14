import smtplib
from email.mime.text import MIMEText
from user_auth import settings


def send_email(token):
    server = smtplib.SMTP_SSL(settings.SMTP_SSL, 465)
    server.login(settings.USR_NAME, settings.USR_PASSWORD)
    msg = MIMEText(f'<a href="http://127.0.0.1:8000/url/verify/{token}">abc</a>', 'html')
    server.sendmail(settings.FROM, settings.TO, msg.as_string())
    server.quit()
