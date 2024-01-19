import tensorflow as tf
import streamlit as st
from streamlit.components import v1 as components
from tensorflow.keras.models import load_model
st.set_page_config(layout="wide")
from data_preprocessing import data_preprocessing


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

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

model12 = load_model("model_12_saved.h5")


# User input for each feature
pclass = st.selectbox('Ticket class: 1 = 1st, 2 = 2nd, 3 = 3rd', [1, 2, 3])
sex = st.selectbox('Sex', ['male', 'female'])
fare = st.slider('Fare', min_value=0.0, max_value=50.0, value=25.0, step=0.5)
age = st.slider('Age', min_value=0.0, max_value=100.0, value=30.0, step=1.0)
sibsp = st.selectbox('Number of Siblings/Spouses Aboard', [0, 1, 2])
parch = st.selectbox('Number of Parents/Children Aboard', [0, 1, 2])


def predict(pclass, sex, fare, age, sibsp, parch):
    # Convert inputs to model's expected format
    pclass = int(pclass)
    sex = str(sex)
    fare = float(fare)
    age = float(age)
    sibsp = int(sibsp)
    parch = int(parch)


    # Prepare the input data in the correct format

    preprocessed_data = data_preprocessing(pclass, sex, fare, age, sibsp, parch)

    # Make prediction
    prediction = model12.predict(preprocessed_data)
    
    return prediction


if st.button('Predict'):
    prediction_float = predict(pclass, sex, fare, age, sibsp, parch)
    prediction_label = "Survived" if prediction_float > 0.5 else "Not Survived"
    st.write(f'Prediction: {prediction_label} ({prediction_float})')
    