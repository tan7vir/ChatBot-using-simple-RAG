import streamlit as st
import requests

# App title
st.set_page_config(page_title="Physics ChatBOT")

st.markdown(
    """
    <style>
    /* Change background color */
    .stApp, .st-emotion-cache-12fmjuu, .st-emotion-cache-128upt6{
        background-color: #507687;
    }

    .stSidebar {
        background-color: #384B70;  /* Sidebar background color */
    }

    .st-ak {
        background-color: #FCFAEE;  /* Main content background color */
    }

    .st-emotion-cache-1ny7cjd {
        background-color: #B8001F;
    }

    .st-emotion-cache-12h5x7g p, .stHeading h1, .stHeading h2, .stHeading h3, .stSelectbox p, .stMarkdown p{
        color: #FCFAEE;
    }

    .st-ak {
        border-radius: 5px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Set backend URL
url = 'http://127.0.0.1:5000/api/generate'

# Sidebar for settings
selected_model = 'gemma2:2b'
with st.sidebar:
    st.title('Physics ChatBOT 🦙')
    st.subheader('Models and parameters')
    selected_model = st.selectbox('Choose a model', ['gemma2:2b', 'gemma2:latest', 'llama3.1:8b'], key='selected_model')

# Display existing chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Function to clear chat history
def clear_chat_history():
    st.session_state.messages = []
    st.session_state.messages.append({"role": "assistant", "content": "How may I assist you today?"})

# Sidebar button to clear chat history
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# User-provided prompt
if prompt := st.chat_input("Enter a message...", key="prompt"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Generate a new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = requests.post(url, json={"prompt": prompt, "model": selected_model})

                if response.status_code == 200:
                    data = response.json()
                    assistant_reply = data.get("response", "No answer provided.")
                else:
                    assistant_reply = "Failed to connect to the server. Please try again later."

                # Store and display assistant's reply
                st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
                st.write(assistant_reply)
