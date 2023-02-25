import streamlit as st
from streamlit.server.server import Server


# Define JavaScript code to get user location
jscode = """
navigator.geolocation.getCurrentPosition(
    function(position) {
        const latitude  = position.coords.latitude;
        const longitude = position.coords.longitude;
        const accuracy  = position.coords.accuracy;
        const location  = {'latitude': latitude, 'longitude': longitude, 'accuracy': accuracy};
        const locationJson = JSON.stringify(location);
        window.parent.postMessage({ location: locationJson }, '*');
    }
);
"""

# Display the JavaScript code using the html component
st.components.v1.html('<script>{}</script>'.format(jscode))

# Wait for the user to share their location
location_json = Server.get_current()._location_request.future.result()

# Parse the JSON data and display it in Streamlit
if location_json:
    location = json.loads(location_json['args']['location'])
    st.write('Latitude:', location['latitude'])
    st.write('Longitude:', location['longitude'])
    st.write('Accuracy:', location['accuracy'])
else:
    st.write('No location data received.')
