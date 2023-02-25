import json
import streamlit as st
from streamlit.components.v1 import html

# 定义获取位置信息的JavaScript代码
jscode = """
async function getLocation() {
    if (navigator.geolocation) {
        try {
            const position = await new Promise((resolve, reject) =>
                navigator.geolocation.getCurrentPosition(resolve, reject)
            );
            const { latitude, longitude, accuracy } = position.coords;
            return { latitude, longitude, accuracy };
        } catch (error) {
            console.error(error);
            return null;
        }
    } else {
        console.error('Geolocation is not supported by this browser.');
        return null;
    }
}

async function sendLocation(location) {
    const response = await fetch('/_set_location', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(location)
    });
    if (!response.ok) {
        console.error(response.statusText);
    }
}

async function main() {
    const location = await getLocation();
    if (location) {
        await sendLocation(location);
    }
}

main();
"""

# 定义在Streamlit应用程序中设置位置信息的回调函数
@st.server_routes('/_set_location')
def set_location():
    location_json = st.request.body.decode('utf-8')
    st.session_state.location = json.loads(location_json)
    return 'OK'

# 在Streamlit应用程序中添加JavaScript代码
html_code = html('<script>{}</script>'.format(jscode), scrolling=False)
st.components.v1.html(html_code)

# 在Streamlit应用程序中获取位置信息
if 'location' in st.session_state:
    location = st.session_state.location
    st.write('Latitude:', location['latitude'])
    st.write('Longitude:', location['longitude'])
    st.write('Accuracy:', location['accuracy'])
else:
    st.write('Location not found.')
