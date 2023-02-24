import os
import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import db
import streamlit as st





my_var = os.environ.get('FIREBASE_KEY')

# 显示环境变量值
st.write(my_var)
