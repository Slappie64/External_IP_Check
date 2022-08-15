# Imports
from requests import get, put
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
current_ip = dns_json['data']

# Check current external IP against GoDaddy DNS Records
if ip_check == current_ip:
    try:
        update_dns = put(url, params = {'domain':'luigi-marino.com'}, headers=headers, field={'data':'1.1.1.1'})
        print(update_dns.text)
    except Exception as ex:
        print('Something went wrong: ', ex)
else:
    print('Yep')


    
# Test Prints
print('External IP: '+ip_check)
#print(secret.api_key)
#print(test)
print('DNS IP: '+current_ip)
