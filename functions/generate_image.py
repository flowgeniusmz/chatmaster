import streamlit as st
from openai import OpenAI
import requests
import cv2
from PIL import Image

client = OpenAI(api_key=st.secrets.openai.api_key_general)
model = st.secrets.openai.model_dalle

def generate_image(vPrompt):

    response = client.images.generate(
        prompt=vPrompt,
        model=model,
        n=1,
        size="1024x1024",
        quality="standard"
    )

    image_url = response.data[0].url

    return image_url

def generate_image_and_save(vPrompt):

    image_url = generate_image(vPrompt=vPrompt)
    
    im = Image.open(requests.get(image_url, stream=True).raw)
    im.save('temp.png')
    
    #img = cv2.imread('temp.png', cv2.IMREAD_UNCHANGED)
    #cv2.imshow(img)
    return image_url

