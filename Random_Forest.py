import tensorflow as tf
import streamlit as st
from streamlit.components import v1 as components
from tensorflow.keras.models import load_model


from data_preprocessing import data_preprocessing

st.set_page_config(layout="wide")

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


st.markdown("""
    <style>
    .element-container {
        margin-bottom: 0px;
    }
    .stSlider, .stSelectbox {
        padding-bottom: 10px;
    }
    .stMarkdown {
        padding-bottom: 1px;
    }
    </style>
    """, unsafe_allow_html=True)


st.markdown("""
    <div style="text-align: center">
        <h1>Using my best Deployed and Saved Random Forest Model</h1>
        <h3>Please select the values that you want, and then press the "predict" button to see if they would survive the titanic</h3>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

# Create a column layout so the text below is less wide
col1, col2, col3 = st.columns([1,6,1])


# User input for each feature
with col2:

    

    st.markdown('<h3 style="color:lightblue;">Ticket class: 1 = 1st, 2 = 2nd, 3 = 3rd</h3>', unsafe_allow_html=True)
    pclass = st.selectbox('',[1, 2, 3])
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown('<h3 style="color:lightblue;">Sex:</h3>', unsafe_allow_html=True)
    sex = st.selectbox('', ['male', 'female'])
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown('<h3 style="color:lightblue;">Fare:</h3>', unsafe_allow_html=True)
    fare = st.slider('', min_value=0.0, max_value=50.0, value=25.0, step=0.5)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown('<h3 style="color:lightblue;">Age (0-100):</h3>', unsafe_allow_html=True)
    age = st.slider('', min_value=0.0, max_value=100.0, value=30.0, step=1.0)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown('<h3 style="color:lightblue;">Number of Siblings/Spouses Aboard:</h3>', unsafe_allow_html=True)
    sibsp = st.selectbox('', [0, 1, 2])
    st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown('<h3 style="color:lightblue;">Number of Parents/Children Aboard:</h3>', unsafe_allow_html=True)
    parch = st.selectbox(' ', [0, 1, 2])
    st.markdown('<hr>', unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")

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


    # Make the button bigger
    st.markdown("""
        <style>
        .stButton>button {
            font-size: 10px;
            padding: 20px 40px;
        }
        </style>
        """, unsafe_allow_html=True)

    if st.button('Predict'):
        prediction_float = predict(pclass, sex, fare, age, sibsp, parch)
        prediction_float = round(prediction_float[0][0] * 100, 2)    # turn to a percentage and round to the nearest hundreth

        if prediction_float > 50:
            st.markdown(f'#### Prediction: <span style="color: green; font-weight: bold;">Your person would have survived the titanic</span>, with a survival rate of {prediction_float}%', unsafe_allow_html=True)
        else:
            st.markdown(f'#### Prediction: <span style="color: red; font-weight: bold;">Your person would not have survived the titanic</span>, with only a survival rate of {prediction_float}%', unsafe_allow_html=True)




# Load part 2
with open('Neural_Network_2.html', 'r') as file:    
    html_content_2 = file.read()

components.html(html_content_2, width = None, height=3700)




