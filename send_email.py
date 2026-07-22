import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "nabil29089@gmail.com"
    password = "dywelspctelvhptq"

    # The receiver can be the same as the username
    receiver = "nabil29089@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)