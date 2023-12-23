import streamlit as st


def st_initialize_sessionstate_initialassistant():

    if "initial_assistant_message" not in st.session_state:
        st.session_state.initial_assistant_message = {
            "role": "assistant",
            "content": "Welcome to FlowGeniusAI. How may I help you?"
        }


def st_initialize_sessionstate_messages_user():
    
    if "messages1_user" not in st.session_state:
        st.session_state.messages1_user = []
    

def st_initialize_sessionstate_messages_assistant():
   
    if "messages1_assistant" not in st.session_state:
        st.session_state.messages1_assistant = []
       

def st_initialize_sessionstate_messages_userandassistant():

    if "messages1" not in st.session_state:
        st.session_state.messages = []




def st_initialize_sessionstate_messages():

    st_initialize_sessionstate_messages_user()
    st_initialize_sessionstate_messages_assistant()
    st_initialize_sessionstate_messages_userandassistant()

