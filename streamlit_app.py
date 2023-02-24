import os
import firebase_admin
import json
import streamlit as st
from firebase_admin import credentials
from firebase_admin import db


from google.oauth2 import service_account


# Get Firebase credentials from environment variable

firebase_key = os.environ.get("FIREBASE_KEY")
cert_dict = json.loads(firebase_key)

with open("mydata-7c783-77425a396005.json", "r") as f:
    data = json.load(f)

# 显示 JSON 数据
st.write(data)
st.write(cert_dict )
