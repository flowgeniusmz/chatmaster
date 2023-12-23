import streamlit as st

def st_display_messages(varMessages):

    for message in varMessages:
        role = message['role']
        
        content = message['content']

        with st.chat_message(role):

            st.markdown(content)


def st_add_message_to_display(varRole, varContent):

    with st.chat_message(varRole):

        st.markdown(varContent)




