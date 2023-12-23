import streamlit as st

def get_response_content(vResponse, vType):

    if vType == "Assistant": 
        content = vResponse.data[0].content[0].text.value
    
    elif vType == "Completion": 
        content = vResponse.choices[0].message.content

    elif vType == "Image":
        content = vResponse.data[0].url

    else:
        content = "Error"
    
    return content
