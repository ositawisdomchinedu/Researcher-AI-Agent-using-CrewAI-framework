import streamlit as st
import yagmail

def send_email_with_attachment(receiver_email, subject, body, attachment_path):
    try:
        sender_email = st.secrets["SENDER_EMAIL"]
        sender_password = st.secrets["SENDER_PASSWORD"]

        yag = yagmail.SMTP(user=sender_email, password=sender_password)
        yag.send(to=receiver_email, subject=subject, contents=body, attachments=attachment_path)
        return "SUCCESS"

    except Exception as e:
        return f"ERROR: {str(e)}"
