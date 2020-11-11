import smtplib
import imghdr
from email.message import EmailMessage

sub = " hello world"
body = "This is interesting"

msg = EmailMessage()

msg['Subject'] = sub
msg['From'] = "rahulgksvv@gmail.com"
msg['To'] = "rahulgksvv@gmail.com"
msg.set_content(body)

with open("rahul photo.jpg",'rb') as f:
    file_data=f.read()
    file_type= imghdr.what(f.name)
    file_name= imghdr.what(f.name)

msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com',465)as smtp:
    smtp.login("rahulgksvv@gmail.com","mxeefpxcoepxobqt") ##email and app password


    smtp.send_message(msg)
