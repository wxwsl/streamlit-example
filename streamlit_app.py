import json
import streamlit as st

# 加载 JSON 文件
with open("mydata-7c783-77425a396005.json") as f:
    data = json.load(f)

# 显示 JSON 数据
st.write(data)
