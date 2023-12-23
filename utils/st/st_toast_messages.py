import streamlit as st

def get_toast_message(vType, vSubject):

    if vType == "Start": 
        toast = st.toast(
            body=f"Running {vSubject.lower()}...",
            icon="🔨"
        )
    
    if vType == "End":
        toast = st.toast(
            body=f"{vSubject} completed!",
            icon="✅"
        )