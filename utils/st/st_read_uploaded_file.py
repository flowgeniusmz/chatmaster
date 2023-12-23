import PyPDF2
import io
import docx
import streamlit as st


def read_pdf(file):
    with io.BytesIO(file.getvalue()) as f:
        reader = PyPDF2.PdfFileReader(f)
        text = ''
        for page in range(reader.numPages):
            text += reader.getPage(page).extractText()
    return text


def read_docx(file):
    doc = docx.Document(io.BytesIO(file.getvalue()))
    text = ''
    for para in doc.paragraphs:
        text += para.text + '\n'
    return text


def read_file(uploaded_file):
    if uploaded_file is not None:
        file_type = uploaded_file.name.split('.')[-1]

        if file_type in ['txt', 'md']:
            return uploaded_file.read().decode('utf-8')
        elif file_type == 'pdf':
            return read_pdf(uploaded_file)
        elif file_type == 'docx':
            return read_docx(uploaded_file)
        else:
            st.error("Unsupported file type")
            return None
    else:
        return None

