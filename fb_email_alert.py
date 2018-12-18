import sendgrid
import os
from sendgrid.helpers.mail import *
from text_bug_alerts import send_error_alert
from read_json import my_email_secret, sendgrid_api_secret

def start_growth():
    sg = sendgrid.SendGridAPIClient(apikey=sendgrid_api_secret)
    from_email = Email("kam@notifications.kameronkales.com")
    to_email = Email(my_email_secret)
    subject = "Your Facebook Growth Hacking Tool Starting Running"
    content = Content("text/plain", "You will get another email when it finishes")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    if response.status_code != 200 | 202:
        print "You have a problem"
        error = "You have a problem in the start of growth"
        send_error_alert(error)
    else:
        print "The growth has begun"

def end_growth():
        sg = sendgrid.SendGridAPIClient(apikey=sendgrid_api_secret)
        from_email = Email("kam@notifications.kameronkales.com")
        to_email = Email(my_email_secret)
        subject = "Your Facebook Growth Hacking Tool Completed Its Task"
        content = Content("text/plain", "You will get another email when it starts again")
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        if response.status_code != 200 | 202:
            print "You have a problem"
            error = "You have a problem in the end of growth"
            send_error_alert(error)
        else:
            print "The growth has completed"
