import streamlit as st
import warnings

# Filter out warnings
warnings.filterwarnings("ignore")

st.title(":fire: Ask Nero:")
st.divider()

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://getwallpapers.com/wallpaper/full/5/2/e/351848.jpg");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

set_bg_hack_url()

# File uploader
uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])
if uploaded_file is not None:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Accept user input
    user_input = st.chat_input("Ask away...")
    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Display chat messages from history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
else:
    st.write("Please upload a PDF document to proceed.")