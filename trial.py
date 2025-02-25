import smtplib
import mimetypes
from email.message import EmailMessage
message = EmailMessage()
sender = "pjenil1609@gmail.com"
recipient = "cvammakwana@gmail.com"
message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Learning to send email from medium.com'
body = """Hello
I am learning to send emails using Python!!!"""
message.set_content(body)
mime_type, _ = mimetypes.guess_type('Jenil.jpg')
mime_type, mime_subtype = mime_type.split('/')
with open('Jenil.jpg', 'rb') as file:
 message.add_attachment(file.read(),
 maintype=mime_type,
 subtype=mime_subtype,
 filename='Jenil.jpg')
print(message)
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_server.set_debuglevel(1)
mail_server.login("pjenil1609@gmail.com", 'ocgvjfhfyfjolodc')
mail_server.send_message(message)
mail_server.quit()
