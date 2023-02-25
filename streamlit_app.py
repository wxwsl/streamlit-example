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
        const event = new CustomEvent("location", {detail: locationJson});
        document.dispatchEvent(event);
    }
);
"""

# Display the JavaScript code using the html component
html_code = html('<script>{}</script>'.format(jscode))

# Define a function to handle custom events sent from JavaScript
@st.cache(allow_output_mutation=True)
def handle_custom_event():
    location_json = st.session_state.location
    if location_json:
        location = json.loads(location_json)
        st.write('Latitude:', location['latitude'])
        st.write('Longitude:', location['longitude'])
        st.write('Accuracy:', location['accuracy'])
    else:
        st.write('No location data received.')

# Add a report context to store session state
add_report_ctx = st.report_thread.add_report_ctx
with add_report_ctx('session state'):
    if 'location' not in st.session_state:
        st.session_state.location = None

# Wait for the custom event to be triggered
document_event = st.bokeh_events().event('location')
if document_event:
    st.session_state.location = document_event['location']

# Handle the custom event
handle_custom_event()
