from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACcca1c745c804b5ba5993e475d916c76c"
auth_token = "cd7acfcc3f4499ef4dda78d6a0852dbe"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="+14344663745",
                                             from_="+14344811688",
                                             body="Hello there!")
