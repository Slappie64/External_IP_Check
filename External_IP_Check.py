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

test = get(url, params = {'domain':'luigi-marino.com'}, headers=headers).text

# Take in information from GoDaddy API and make it usable
test = test.replace('[','')
test = test.replace(']','')
api_json = json.loads(test)

current_ip = api_json['data']

if ip_check != current_ip:
    print('Nope')
else:
    print('Yep')
# Test Prints
#print(ip_check)
#print(secret.api_key)
#print(test)
#print(current_ip)
