import streamlit as st

def st_create_message(varRole, varContent): 

    message = {
        "role": varRole,
        "content": varContent
    }

    return message

   

