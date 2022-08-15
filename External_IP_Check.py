import secret
from godaddypy import Client, Account

account = Account(api_key = secret.public_key, api_secret = secret.secret_key)

client = Client(account)

print(client.get_domains())
