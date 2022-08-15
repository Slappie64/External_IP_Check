from requests import get
import secret
import json

# Current saved external IP Address
ip_saved = '1.1.1.1' 

# Get current external IP Address
ip_check = get('https://api.ipify.org').text

# GoDaddy API call
headers = {'Authorization': 'sso-key {}:{}'.format(secret.api_key, secret.secret_key)}
url = 'https://api.godaddy.com/v1/domains/luigi-marino.com/records/A/%40'

test = get(url, params = {'domain':'luigi-marino.com'}, headers=headers).text

# Check if IP addresses match
if ip_check != ip_saved:
    print('nope')

# Take in information from GoDaddy API and make it usable
test = test.replace('[','')
test = test.replace(']','')
api_json = json.loads(test)

# Test Prints
print(ip_check)
print(secret.api_key)
print(test)
print(api_json['data'])
