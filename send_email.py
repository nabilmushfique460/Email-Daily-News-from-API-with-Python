import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    # Get username and password from Streamlit secrets
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    # The receiver can be the same as the username
    receiver = username

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
