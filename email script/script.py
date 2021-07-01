import smtplib
import os
import pandas as pd
from email.message import EmailMessage

#establishing connection
smtp= smtplib.SMTP_SSL('smtp.gmail.com',465)
smtp.login("your email address","password")

#Importing email list from CSV file
email_list=pd.read_csv(os.path.join((os.getcwd), 'emails.csv'))
emails=email_list['EMAIL']

msg=EmailMessage()    
msg.set_content('Body of the  mail')
msg['Subject']="Subject of the mail"
msg['From']="Sender's email address"

#Add file to be attached
file='file.pdf'
with open(file,'rb') as f:
    file_data=f.read()
    file_name=f.name
msg.add_attachment(file_data, maintype='application', subtype='octet-stream',filename=file_name)
for contact in emails:
   msg['To']=contact
   smtp.send_message(msg)