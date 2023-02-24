import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



# 获取Firebase服务帐户密钥
firebase_key = os.environ.get("FIREBASE_KEY")
cert_dict = json.loads(firebase_key)

# 初始化Firebase应用程序
cred = credentials.Certificate(cert_dict)
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
