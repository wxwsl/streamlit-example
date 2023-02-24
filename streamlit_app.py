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
cred = credentials.Certificate(cert_dict)

st.write(cert_dict )
