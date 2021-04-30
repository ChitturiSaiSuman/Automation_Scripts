# Send an Email to Gmail Clients
#!/usr/bin/python3
import csv
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime

def with_attachment(fromaddr,toaddr,password):
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	subject = input("Enter Subject (Should be One-liner): ")
	msg['Subject'] = subject
	body = ""
	print("Enter Body of Email. Enter ` to stop reading.")
	s=input()
	while '`' not in s:
		body+=s+'\n'
		s=input()
	if len(s)!=1:
		body+=s
	msg.attach(MIMEText(body,'plain'))
	filename = input("Enter File name with Extension: ")
	path = input("Enter Name of File with Path: ")
	attachment = open(path,"rb")
	p = MIMEBase('applicaton','octet-stream')
	p.set_payload((attachment).read())
	encoders.encode_base64(p)
	p.add_header('Content-Disposition',"attachment; filename = %s"%(filename))
	msg.attach(p)
	s = smtplib.SMTP('smtp.gmail.com',587)
	print("Performing a TLS handshake")
	s.starttls()
	s.login(fromaddr,password)
	print("Logged in Successfully!")
	text = msg.as_string()
	print("Sending Email...")
	s.sendmail(fromaddr,toaddr,text)
	print("Email Sent")
	s.quit()
	print()
	print("Details of the Mail: ")
	print()
	print("From Address: "+fromaddr)
	print()
	print("To Address: "+toaddr)
	print()
	print("Subject: "+subject)
	print()
	print("Body: "+'\n'+body)
	print()
	print("Attachments: "+filename)
	print()
	print("Sent at: "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	print()
	print("Sent Sucessfully!")
	print()

def without_attachment(fromaddr,toaddr,password):
	s = smtplib.SMTP('smtp.gmail.com',587)
	s.starttls()
	s.login(fromaddr,password)
	print("Enter Message. Include the Subject in the message itself. Enter ` to stop reading.")
	message = ""
	text = input()
	while '`' not in text:
		message+=text+'\n'
		text=input()
	message+=text
	s.sendmail(fromaddr,toaddr,message)
	s.quit()
	print("Details of the Mail: ")
	print()
	print("From Address: "+fromaddr)
	print()
	print("To Address: "+toaddr)
	print()
	print("Message: \n"+message)
	print()
	print("Attachment: NONE")
	print()
	print("Sent at: "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	print("Sent Successfully!")
def main():
	flag = True
	while flag:
		fromaddr = input("Enter Email address of the Sender: ")
		toaddr = input("Enter Email address of the Receiver: ")
		password = input("Enter Password: ")
		if input("Do you want to attach any files(Y/N): ") in "YesYESyes":
			with_attachment(fromaddr,toaddr,password)
		else:
			without_attachment(fromaddr,toaddr,password)
		flag = input("Do you want to send another(Y/N): ") in "YESyesYes"

main()
