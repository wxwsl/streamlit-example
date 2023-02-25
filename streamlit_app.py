import streamlit as st
from streamlit.components.v1 import html

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

# Wait for the user to share their location
location_json = st.wait_for_custom_request('location')

# Parse the JSON data and display it in Streamlit
if location_json:
    location = json.loads(location_json['args']['location'])
    st.write('Latitude:', location['latitude'])
    st.write('Longitude:', location['longitude'])
    st.write('Accuracy:', location['accuracy'])
else:
    st.write('No location data received.')
