
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

Sender = input("please input your correct email : ")
my_password = input("enter your Password : ")
To = input("enter Receiver's Gmail :  ")

msg = MIMEMultipart('alternative')
msg['Subject'] = input("Input the Subject :")
msg['From'] = Sender
msg['To'] = To

message = input("please input your message Here !: ")
msg.attach(MIMEText(message, 'plain'))
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(Sender, my_password)

s.sendmail(Sender, To, msg.as_string())
s.quit()

