from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="myapp")
import streamlit as st

# Prompt user for their address
address = st.text_input('Please enter your address')

# When user clicks the 'Submit' button, get their location
if st.button('Submit'):
    location = geolocator.geocode(address)
    if location:
        st.write('Your latitude:', location.latitude)
        st.write('Your longitude:', location.longitude)
    else:
        st.write('Sorry, we could not find your location.')
