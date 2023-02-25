import streamlit as st
from streamlit.components.v1 import html

js_code = """
navigator.geolocation.getCurrentPosition(function(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    const accuracy = position.coords.accuracy;
    const data = {'latitude': latitude, 'longitude': longitude, 'accuracy': accuracy};
    const event = new CustomEvent('location', {detail: data});
    document.dispatchEvent(event);
});
"""

html_code = html('<script>{}</script>'.format(js_code))
