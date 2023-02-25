import ipinfo

import requests

def get_client_ip():
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0'})
    ip_request = requests.get('https://api.ipify.org', headers=headers)
    return ip_request.text

client_ip = get_client_ip()
print("Client IP Address:", client_ip)



