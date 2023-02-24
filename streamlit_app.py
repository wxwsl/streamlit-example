import os
import firebase_admin
import json
import streamlit as st
from firebase_admin import credentials
from firebase_admin import db
os.environ.get("FIREBASE_KEY")
cred=os.environ.get("FIREBASE_KEY")
firebase_key_json = json.loads(os.environ.get("FIREBASE_KEY"))
#cred = service_account.Credentials.from_service_account_info(firebase_key_json)


st.write(cred)
