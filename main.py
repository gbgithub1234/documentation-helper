import streamlit as st

# Set the new Streamlit app URL
new_url = "https://chatbot-pinecone-update-xfbotzptgbtt2kk5e46pfg.streamlit.app/"

# Delay redirect by 3 seconds to avoid redirect loops
st.markdown(f"""
    <meta http-equiv="refresh" content="3; url={new_url}">
    <h3>🔁 Redirecting you to the updated chatbot...</h3>
    <p>This app has moved to a new address.</p>
    <p>If you're not automatically redirected, <a href="{new_url}">click here</a>.</p>
""", unsafe_allow_html=True)
