import tensorflow as tf
import streamlit as st
from streamlit.components import v1 as components
from tensorflow.keras.models import load_model
st.set_page_config(layout="wide")
from data_preprocessing import data_preprocessing


# Load part 1
with open('Neural_Network_1.html', 'r') as file:    
    html_content_1 = file.read()

components.html(html_content_1, width = None, height=1000)


#Add some spacing between elements on the website
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")


st.markdown("# Using my Deployed and Saved Neural Network (model 12, my best model)")
st.markdown("### Please select the values that you want, and then press the \"predict\" button to see if they would survive the titanic")

st.write("")
st.write("")
st.write("")

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

    model12 = load_model("model_12_saved.h5")

    # Make prediction
    prediction = model12.predict(preprocessed_data)
    
    return prediction


if st.button('Predict'):
    prediction_float = predict(pclass, sex, fare, age, sibsp, parch)
    prediction_float = round(prediction_float[0][0] * 100, 2)    # turn to a percentage and round to the nearest hundreth

    if prediction_float > 50:
        st.markdown(f'Prediction: <span style="color: green; font-weight: bold;">Your person would have survived</span>, with a survival rate of {prediction_float}%', unsafe_allow_html=True)
    else:
        st.markdown(f'Prediction: <span style="color: red; font-weight: bold;">Your person would have not survived</span>, with only a survival rate of {prediction_float}%', unsafe_allow_html=True)




# Load part 2
with open('Neural_Network_2.html', 'r') as file:    
    html_content_2 = file.read()

components.html(html_content_2, width = None, height=3700)




