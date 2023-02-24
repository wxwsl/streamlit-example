import os
import firebase_admin
import json
import streamlit as st
from firebase_admin import credentials
from firebase_admin import db


from google.oauth2 import service_account


# Get Firebase credentials from environment variable
firebase_key_json = json.loads(os.environ.get("FIREBASE_KEY"))
firebase_credentials = credentials.Certificate(firebase_key_json)
st.write(cred)
