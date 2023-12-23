import streamlit as st

def st_append_message(varMessages, varRole, varContent): 

    message = {
        "role": varRole,
        "content": varContent
    }

    messages = varMessages.append(message)

    return messages


