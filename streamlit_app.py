import requests
import streamlit as st
ip_request = requests.get('https://ipapi.co/ip/')
client_ip = ip_request.text
print("Client IP Address:", client_ip)

st.write(client_ip)
