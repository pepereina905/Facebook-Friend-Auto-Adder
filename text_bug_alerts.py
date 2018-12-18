import os
from twilio.rest import Client
from read_json import account_sid_secret, auth_token_secret, your_cell_secret, your_twilio_number_secret

account_sid = account_sid_secret
auth_token  = auth_token_secret
your_cell = your_cell_secret
your_twilio_number = your_twilio_number_secret

client = Client(account_sid, auth_token)


def send_error_alert(error):
    message = client.messages.create(
        to=your_cell,
        from_=your_twilio_number,
        body=error)
    print message.sid
