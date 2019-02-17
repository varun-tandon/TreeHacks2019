import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey='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')
from_email = Email("yourconstiuents@insession.com")
to_email = Email("roberto.lama18@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
