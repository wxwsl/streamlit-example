import firebase_admin
from firebase_admin import credentials

# 初始化 Firebase 应用程序
cred = credentials.Certificate("mydata-7c783-77425a396005.json")
try:
    firebase_admin.initialize_app(cred)
except ValueError:
    pass
