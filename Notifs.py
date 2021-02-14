
import Keys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_address = Keys.GMAIL_USERNAME
sender_pass = Keys.GMAIL_PASSWORD
receiver_address = Keys.GMAIL_USERNAME

def send(subject, content):
   #Setup the MIME
   message = MIMEText(content)
   message['From'] = sender_address
   message['To'] = receiver_address
   message['Subject'] = subject

   #Create SMTP session for sending the mail
   session = smtplib.SMTP('smtp.gmail.com', 587)
   session.starttls()
   session.login(sender_address, sender_pass)
   text = message.as_string()
   session.sendmail(sender_address, receiver_address, text)
   session.quit()