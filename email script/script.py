import smtplib
from email.message import EmailMessage
msg=EmailMessage()
msg['Subject']="Subject of the mail"
msg['From']="Sender's email address"
msg['To']="Receiver's email address"
msg.set_content('Body of the  mail')
#Add file to be attached
file='file.pdf'
with open(file,'rb') as f:
    file_data=f.read()
    file_name=f.name
msg.add_attachment(file_data, maintype='application', subtype='octet-stream',filename=file_name)
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    

    smtp.login("your email address","password")

    
    smtp.send_message(msg)