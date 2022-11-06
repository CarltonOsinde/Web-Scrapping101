import smtplib
import ssl #standard  python libary to send emails via python

#standard variable declaration
host = "smtp.gmail.com"
port = 468

#Email credentials
password = ""
username = "carltonosinde@gmail.com"

receiver = "carltonosinde@gmail.com"
context = ssl.create_default_context()

message = """

Hello Motherfuckers!

"""

with smtplib.SMTP_SSL(host,port,context=context) as server:
    server.login(username, password)
    server.sendmail(username,receiver, message)
