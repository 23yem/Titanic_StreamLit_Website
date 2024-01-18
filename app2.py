import streamlit as st


st.title('Titanic Survival Prediction')

# Load HTML file
with open('Titanic_Website_V2\index.html', 'r') as file:
    html_content = file.read()

# Display HTML
st.markdown(html_content, unsafe_allow_html=True)