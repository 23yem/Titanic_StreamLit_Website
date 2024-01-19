import tensorflow as tf
import streamlit as st
from streamlit.components import v1 as components
from tensorflow.keras.models import load_model


st.set_page_config(layout="wide")

# Load HTML file
with open('index.html', 'r') as file:    
    html_content = file.read()

components.html(html_content, width = None, height=1900)


#This is center the image (add invisible columns on the right and left of image)
col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.image("high_score_of_80.622.jpg")

with col3:
    st.write("")


