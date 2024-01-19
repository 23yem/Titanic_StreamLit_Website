import tensorflow as tf
import streamlit as st
from streamlit.components import v1 as components
from tensorflow.keras.models import load_model
st.set_page_config(layout="wide")


# Load HTML file
with open('index.html', 'r') as file:    
    html_content = file.read()

components.html(html_content, width = None, height=1200)

st.image("high_score_of_80.622.jpg")

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

model12 = load_model("model_12_saved.h5")


# User input for each feature
pclass = st.selectbox('Passenger Class', [1, 2, 3], format_func=lambda x: f'Class {x}')
sex = st.selectbox('Sex', ['Male', 'Female'])
fare = st.slider('Fare', min_value=0.0, max_value=50.0, value=25.0, step=0.5)
age = st.slider('Age', min_value=0.0, max_value=100.0, value=30.0, step=1.0)
sibsp = st.selectbox('Number of Siblings/Spouses Aboard', [0, 1, 2])
parch = st.selectbox('Number of Parents/Children Aboard', [0, 1, 2])


def predict(pclass, sex, fare, age, sibsp, parch):
    # Convert inputs to model's expected format
    # ...


    # Prepare the input data in the correct format
    input_data = [pclass, sex, fare, age, sibsp, parch]


    # Make prediction
    prediction = model12.predict([input_data])
    return prediction


if st.button('Predict'):
    prediction = predict(pclass, sex, fare, age, sibsp, parch)
    st.write(f'Prediction: {"Survived" if prediction[0] == 1 else "Not Survived"}')
    