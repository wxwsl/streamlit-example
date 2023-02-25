import streamlit as st
from streamlit.components.v1 import html

# 定义 JavaScript 代码，获取用户地理位置
jscode = """
navigator.geolocation.getCurrentPosition(
    function(position) {
        const latitude  = position.coords.latitude;
        const longitude = position.coords.longitude;
        const accuracy  = position.coords.accuracy;
        const location  = {'latitude': latitude, 'longitude': longitude, 'accuracy': accuracy};
        const locationJson = JSON.stringify(location);
        window.location.href = "streamlit://location=" + encodeURIComponent(locationJson);
    }
);
"""

# 显示 JavaScript 代码
html_code = html('<script>{}</script>'.format(jscode))

# 等待用户分享其位置
location_json = st._get_streamlit_share_request('location')

# 解析 JSON 数据并在 Streamlit 上显示
if location_json:
    location = json.loads(location_json['args']['location'])
    st.write('Latitude:', location['latitude'])
    st.write('Longitude:', location['longitude'])
    st.write('Accuracy:', location['accuracy'])
else:
    st.write('No location data received.')
