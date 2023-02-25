import requests
import streamlit as st
ip_request = requests.get('https://ipapi.co/ip/')
client_ip = ip_request.text
print("Client IP Address:", client_ip)

st.write(client_ip)


import ipinfo
access_token = 'fd7290568d6d4f'
handler = ipinfo.getHandler(access_token)
ip_address = '216.239.36.21'
details = handler.getDetails(client_ip)
details.city
details.loc
