import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject']="Crop Training Invite"
msg['From']='learnpython2019@gmail.com'
msg['to']='learnpython2019@gmail.com'
msg.set_content("Test Email from Automation team")

with open("email.txt") as myfile:
     data = myfile.read()
     msg.set_content(data)

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login('learnpython2019@gmail.com',"password@123")
server.send_message(msg)
server.quit()
