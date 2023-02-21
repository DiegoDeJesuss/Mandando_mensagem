from twilio.rest import Client

account_sid = 'AC2892ffb304da3638dfdc7482eddebc2a'
auth_token = 'ec719329dd1e2411b42c2dd74ebfcbb3'
client = Client(account_sid, auth_token)


remetente = '+13024055027'
destino = '+5521994780962'

message = client.messages.create(
    to=destino,
    from_= remetente,
    body="Fala Diego!"


)