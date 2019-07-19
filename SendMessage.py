from twilio.rest import Client

account_sid="---Enter account sid---"
auth_token="---enter auth token----"
client=Client(account_sid,auth_token)
message=client.messages.create(
    body="Hi this is self generated message by nehal!",
    to="---enter receiver number---",
    from_="---enter your twilio number---")

print (message.sid)
