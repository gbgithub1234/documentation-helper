import streamlit as st

# Target URL for the new app
new_url = "https://chatbot-pinecone-update-xfbotzptgbtt2kk5e46pfg.streamlit.app/"

# Instant JavaScript redirect (no delay)
st.markdown(f"""
    <h3>🔁 Redirecting to the updated chatbot...</h3>
    <p>If you're not automatically redirected, <a href="{new_url}">click here</a>.</p>

    <script>
        window.location.href = "{new_url}";
    </script>
""", unsafe_allow_html=True)
