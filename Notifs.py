import Keys
import smtplib

def send(message):
   to_number = Keys.GMAIL_USERNAME
   auth = (Keys.GMAIL_USERNAME, Keys.GMAIL_PASSWORD)

   server = smtplib.SMTP(Keys.GMAIL_USERNAME, 587 )
   server.starttls()
   server.login(auth[0], auth[1])

   server.sendmail( auth[0], to_number, message)