import os
from twilio.rest import Client




# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

def sms_all():
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)


    message = client.messages \
        .create(
                body="there's a game over xx",
                from_='+16467989631',
                to= '+18475323886',
            )
    print(message.sid)