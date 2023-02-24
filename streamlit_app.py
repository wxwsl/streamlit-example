import os
import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import db


firebase_key_json = json.loads(os.environ.get("FIREBASE_KEY"))

st.write(firebase_key_json)
