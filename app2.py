import streamlit as st
from streamlit.components import v1 as components

#st.title('Titanic Survival Prediction')

# # Load HTML file
# with open('C:\\Kaggle Machine Learning\\Titanic_StreamLit_Website\\Neural_Network.html', 'r') as file:    
#     html_content = file.read()

# # print(html_content)
# # Display HTML
# #st.markdown(html_content, unsafe_allow_html=True)

# components.html(html_content, width = 1000, height=10000)




# Create three columns
left_spacer, center_content, right_spacer = st.beta_columns((1, 2, 1))

# Use the center column to display your HTML content
with center_content:
    # Define the HTML with centered content using CSS
    with open('C:\\Kaggle Machine Learning\\Titanic_StreamLit_Website\\Neural_Network.html', 'r') as file:    
        html_content = file.read()

        # Render the HTML content
        components.html(html_content)
