import streamlit as st

# Target URL for the new app
new_url = "https://chatbot-pinecone-update-xfbotzptgbtt2kk5e46pfg.streamlit.app/"

st.title("🚨 This App Has Moved...")

st.markdown("""
The SFU Document Chatbot has been updated and moved to a new address.

Please click the button below to access the latest version:
""")

st.link_button("🔗 Go to New Chatbot", new_url)

st.markdown(f"""
If the button doesn't work, [click here]({new_url}) to go directly.
""")
