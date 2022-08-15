from requests import get

# Current saved external IP Address
ip_saved = '1.1.1.1' 

# Get current external IP Address
ip_check = get('https://api.ipify.org').text

# GoDaddy API call


# Check if IP addresses match
if ip_check != ip_saved:
    print('nope')

# Test Prints
print(ip_check)
