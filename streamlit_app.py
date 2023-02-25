import streamlit as st
from streamlit.components.v1 import html
import json

# Define JavaScript code to get user location
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

# Display the JavaScript code using the html component
html_code = html('<script>{}</script>'.format(jscode))

# Define a callback function to handle the custom message
@st.cache(allow_output_mutation=True)
def get_location():
    return {}

def handle_message(msg):
    if 'location' in msg:
        location = json.loads(msg['location'])
        get_location()['location'] = location

# Register the callback function with Streamlit
st._legacy_chrome.message_loop.register_callback("location", handle_message)

# Display the JavaScript code and wait for the user to share their location
st.components.v1.html(html_code)

# Wait for the location data to be available
location_data = get_location()['location']
if location_data:
    st.write('Latitude:', location_data['latitude'])
    st.write('Longitude:', location_data['longitude'])
    st.write('Accuracy:', location_data['accuracy'])
else:
    st.write('No location data received.')
