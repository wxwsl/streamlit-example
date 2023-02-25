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


try:
    firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mydata-7c783-default-rtdb.firebaseio.com'
})
except ValueError:
    pass

# 写入数据
ref = db.reference('/')
###ref.set({
#    'group1': {
 #######       'name': 'Group 1',
#        'description': 'This is group 1'
 #####   },
 ######   'group2': {
  ####      'name': 'Group 2',
  ###      'description': 'This is group 2'
   ## }
#})
import datetime

# 获取当前时间
now = datetime.datetime.now()

# 将时间转换为字符串
time_str = now.strftime("%Y-%m-%d %H:%M:%S")


# 创建输入文本框
st.header('Add new data')
name = st.text_input('Name')
age = st.number_input('Age', min_value=0, max_value=120)
email = st.text_input('Email')

# Define behavior when user clicks the "Add" button
if st.button('Add'):
    # Define new data to be added
    new_data = {
        'name': name,
        'age': age,
        'email': email
    }

    # Push the new data to the database with a new unique key
    new_ref = ref.push(new_data)
    st.success('New data added with key: {}'.format(new_ref.key))



import pandas as pd


data = ref.get()
df = pd.DataFrame.from_dict(data, orient='index')
st.write(df)


data = ref.get()

data_dict = json.loads(json.dumps(data))

if data_dict:
    for key, value in data_dict.items():
        st.write('Key:', key)
        st.write('Name:', value['name'])
        st.write('Age:', value['age'])
        st.write('Email:', value['email'])
        st.write('---')
else:
    st.write('No data found')

