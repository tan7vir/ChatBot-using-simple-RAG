
# Import necessary libraries
import streamlit as st
import requests

# Set backend URL
url = 'http://127.0.0.1:5000/api/generate'
fetch_collection_url = 'http://127.0.0.1:5000/api/fetch_collection'
fetch_chat_url = 'http://127.0.0.1:5000/api/fetch_chat'
delete_chat_url = 'http://127.0.0.1:5000/api/delete_chat_'
add_response_url = 'http://127.0.0.1:5000/api/add_response'

# Initialize variable_name for the chat history
        # Later I can add multiple chat history
        # using this variable_name as a array.
variable_name = ""


# App title
st.set_page_config(page_title="Physics ChatBOT")

# Function to get the collection name
def get_collection():
    response = requests.post(fetch_collection_url)

    if response.status_code == 200:
        data = response.json()
        return data[0]
    else:
        return "empty"

# Function to get the chat history
def get_chat_history():
    response = requests.post(fetch_chat_url, json={"collection_name": variable_name})

    if response.status_code == 200:
        data = response.json()
        
        if isinstance(data, list):
            chats = [{'role': item.get('role'), 'content': item.get('content')} for item in data]

            st.session_state.messages = []
            for char in chats:
                st.session_state.messages.append(char) 
        else:
            print("Data is not in the expected format or is empty.")
    else:
        print("Failed to connect to the server. Please try again later.")

# Get the collection name from the server
variable_name = get_collection()

# Neccessary CSS for the app
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

    .st-emotion-cache-1rsyhoq p {
        # display: none; 
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
    response = requests.post(delete_chat_url, json={"collection_name": variable_name})

    if response.status_code == 200:
      
        get_collection()
        get_chat_history()
    else:
        print("Failed to connect to the server. Please try again later.")



# For the chat history buttons
if ( variable_name != "empty" or variable_name != ""):
    st.sidebar.button(variable_name, on_click=get_chat_history, key="chat_history_1")


# Sidebar button to clear chat history
st.sidebar.button('Clear Chat History', on_click=clear_chat_history, key="clear_chat_history")


# User-provided prompt
if prompt := st.chat_input("Enter a message...", key="prompt"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Generate a new response if last message is not from assistant
    assistant_reply = ""
    if st.session_state.messages[-1]["role"] != "assistant":
        assistant_reply = "Thinking..."
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = requests.post(url, json={"prompt": prompt, "model": selected_model})

                if response.status_code == 200:
                    data = response.json()
                    assistant_reply = data.get("response", "No answer provided.")
                else:
                    assistant_reply = "Failed to connect to the server. Please try again later."
                
                response2 = requests.post(add_response_url, json={"content": prompt, "AssisContent": assistant_reply})
                if response2.status_code == 200:
                    print("Success")
                else:   
                    print("Failed to connect to the server. Please try again later.")

                # Store and display assistant's reply
                st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
                st.write(assistant_reply)
