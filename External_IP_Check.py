import secret
from godaddypy import Client, Account
from requests import get

# Configure account details
account = Account(api_key=secret.public_key, api_secret=secret.secret_key)
client = Client(account)

# Get current DNS record and assign to dns_ip
dns_ip = client.get_records('luigi-marino.com', record_type='A')[0]['data']

# Get current external IP address and assign to ext_ip
ext_ip = get('https://api.ipify.org').text

# Check whether the two IP addresses match
if ext_ip != dns_ip:
    client.update_ip(ext_ip, domains=['luigi-marino.com'])
    

# Test Outputs
# print(client.get_domains())
print(client.get_records('luigi-marino.com', record_type='A'))
print('DNS IP: '+dns_ip)
print('EXT IP: '+ext_ip)
