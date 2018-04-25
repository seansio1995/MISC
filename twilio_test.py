from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="+14344663745",
                                             from_="+14344811688",
                                             body="Hello there!")
