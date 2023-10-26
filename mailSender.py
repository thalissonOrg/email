import smtplib
import os
import email.message

# Get email credentials and other information from environment variables
from_email = os.environ.get('EMAIL_USERNAME')
password = os.environ.get('EMAIL_PASSWORD')
to_email = os.environ.get('TO_EMAIL')
message = os.environ.get('MESSAGE')
subject = os.environ.get('SUBJECT')

# Create an email message
msg = email.message.Message()
msg.set_payload(subject)
msg['Subject'] = message


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(from_email, password)
server.sendmail(from_email, to_email, msg.as_string())
server.rset()
server.quit()
