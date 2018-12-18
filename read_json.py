import simplejson as json

with open('variables.json') as data_file:
    data = json.load(data_file)

fb_email_secret = data['fb_email']
fb_password_secret = data['fb_password']
lab_coat_secret = data['lab_coat']
my_email_secret = data['my_email']
sendgrid_api_secret = data['sendgrid_api']
your_cell_secret = data['your_cell']
your_twilio_number_secret = data['your_cell']
account_sid_secret = data['account_sid']
auth_token_secret = data['auth_token']
