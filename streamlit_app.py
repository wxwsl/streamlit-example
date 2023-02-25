

import streamlit as st
from streamlit import Server
import requests

# Get the client's IP address from the request headers
def get_client_ip():
    session_id = st.session_state.report_id
    ctx = get_report_ctx()
    if ctx is None:
        return None
    this_session = Server.get_current()._get_session_info(session_id)
    if this_session is None:
        return None
    request_headers = this_session.ws.request.headers
    return request_headers.get("X-Forwarded-For", "").split(",")[-1].strip()

client_ip = get_client_ip()
st.write('Client IP Address:', client_ip)
