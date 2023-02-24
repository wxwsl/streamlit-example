import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# 初始化 Firebase 应用程序
cred = credentials.Certificate("mydata-7c783-77425a396005.json")
try:
    firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mydata-7c783.firebaseio.com'
})
except ValueError:
    pass
# 连接到 Realtime Database
ref = db.reference('/')

# 读取数据
data = ref.get()
