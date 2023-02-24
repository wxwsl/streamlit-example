import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# 初始化 Firebase 服务帐户凭据
cred = credentials.Certificate("mydata-7c783-77425a396005.json")
default_app = firebase_admin.initialize_app(cred)
