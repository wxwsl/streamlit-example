import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

firebase_key = os.environ.get("FIREBASE_KEY")
cred = credentials.Certificate(firebase_key)
try:
    firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mydata-7c783-default-rtdb.firebaseio.com'
})
except ValueError:
    pass

# 写入数据
ref = db.reference('/')
ref.set({
    'group1': {
        'name': 'Group 1',
        'description': 'This is group 1'
    },
    'group2': {
        'name': 'Group 2',
        'description': 'This is group 2'
    }
})

import streamlit as st
import pandas as pd


data = ref.get()
df = pd.DataFrame.from_dict(data, orient='index')
st.write(df)
