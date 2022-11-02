import smtplib
import ssl
from email.message import EmailMessage


subject  = "Email from the project bypython"

body = " Test email fromthe aplication that wqe are trying to build for creating from Python!"
sender_email =  "yaveloper@gmail.com"
receiver_email =  "dreiko200590@hotmail.com"
password = input("Please enter the password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject