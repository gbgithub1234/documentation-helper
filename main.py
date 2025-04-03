import streamlit as st

# Set the URL for the new app
new_url = "https://chatbot-pinecone-update-xfbotzptgbtt2kk5e46pfg.streamlit.app/"

# HTML-based auto-redirect
st.markdown(f"""
    <meta http-equiv="refresh" content="0; url={new_url}">
    <h3>🚀 This app has moved!</h3>
    <p>You are being redirected to the new version of the chatbot.</p>
    <p>If you're not redirected automatically, <a href="{new_url}">click here</a>.</p>
""", unsafe_allow_html=True)
