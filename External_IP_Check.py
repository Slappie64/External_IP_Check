# Imports
from requests import get
import secret
import json

# Current saved external IP Address
#ip_TEST = '1.1.1.1' 

# Get current external IP Address
ip_check = get('https://api.ipify.org').text

# GoDaddy API call
headers = {'Authorization': 'sso-key {}:{}'.format(secret.api_key, secret.secret_key)}
url = 'https://api.godaddy.com/v1/domains/luigi-marino.com/records/A/%40'

# Get raw DNS information from GoDaddy API
dns_raw = get(url, params = {'domain':'luigi-marino.com'}, headers=headers).text

# Take in raw information from GoDaddy API and turn it into a useable json string
dns_raw = dns_raw.replace('[','')
dns_raw = dns_raw.replace(']','')
dns_json = json.loads(dns_raw)

# Get the current name from the json data
current_ip = api_json['data']

# Check current external IP against GoDaddy DNS Records
if ip_check != current_ip:
    print('Nope')
else:
    print('Yep')

    
# Test Prints
#print(ip_check)
#print(secret.api_key)
#print(test)
#print(current_ip)
