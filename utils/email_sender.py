import os
import yagmail
from config.settings import SENDER_EMAIL, SENDER_PASSWORD

def send_email_with_attachment(receiver_email, subject, body, attachment_path):
    try:
        yag = yagmail.SMTP(user=SENDER_EMAIL, password=SENDER_PASSWORD, oauth2_file=False)
        yag.send(to=receiver_email, subject=subject, contents=body, attachments=attachment_path)
        return "SUCCESS"

    except Exception as e:
        return f"ERROR: {str(e)}"
