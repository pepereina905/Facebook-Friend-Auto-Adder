import sendgrid
import os
from sendgrid.helpers.mail import *
from text_bug_alerts import send_error_alert
from read_json import my_email_secret, sendgrid_api_secret

def email_test_alert(ok):
    sg = sendgrid.SendGridAPIClient(apikey=sendgrid_api_secret)
    from_email = Email("kam@notifications.kameronkales.com")
    to_email = Email(my_email_secret)
    subject = "Your Email Test Has Been Queued"
    content = Content("text/plain", "You are welcome")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    if response.status_code != 200 | 202:
        print "You have a problem"
        error = "You have a problem in the start of growth"
        send_error_alert(error)
    else:
        print "The growth has begun"
