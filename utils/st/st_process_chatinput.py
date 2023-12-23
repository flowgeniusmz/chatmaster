import streamlit as st
from st_display_messages import st_add_message_to_display

def st_process_chatinput():

    if prompt := st.chat_input(placeholder="Enter your message here..."): 
        
        st_add_message_to_display("user", prompt)

