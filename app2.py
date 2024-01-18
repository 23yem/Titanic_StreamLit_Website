import streamlit as st
from streamlit.components import v1 as components
st.set_page_config(layout="wide")

#st.title('Titanic Survival Prediction')

# # Load HTML file
# with open('C:\\Kaggle Machine Learning\\Titanic_StreamLit_Website\\Neural_Network.html', 'r') as file:    
#     html_content = file.read()

# # print(html_content)
# # Display HTML
# #st.markdown(html_content, unsafe_allow_html=True)


# components.html(html_content, width = None, height=10000)




# # Create three columns
# left_spacer, center_content, right_spacer = st.beta_columns((1, 2, 1))

# # Use the center column to display your HTML content
# with center_content:
#     # Define the HTML with centered content using CSS
#     with open('C:\\Kaggle Machine Learning\\Titanic_StreamLit_Website\\Neural_Network.html', 'r') as file:    
#         html_content = file.read()

#         # Render the HTML content
#         components.html(html_content)





# Define URLs for the navigation bar based on your actual HTML content
urls = {
    "Home": "index.html",  # Replace with your actual home URL
    "GitHub Repository": "https://github.com/23yem/Final-Titanic-Machine-Learning",  # Replace with your actual GitHub URL
    "Neural Networks": "Neural_Network.html",  # Replace with the actual URL
    #"Gradient Boosted Trees": "https://www.gradientboostedtrees.com",  # Replace with the actual URL
    #"Random Forest": "https://www.randomforest.com"  # Replace with the actual URL
}

# Sidebar navigation
st.sidebar.title("Navigation")
for title, url in urls.items():
    if st.sidebar.button(title):
        # This will open the URL in a new tab
        js = f"window.open('{url}')"  # JavaScript to open a new tab
        st.components.v1.html(f'<img src onerror="{js}">', height=0, width=0)

# Main content area
st.title("Neural Network Models")  # The main title of the page

# Section for Neural Network Model
st.header("Neural Network Model")  # Section title
st.subheader("My primary model")  # Section subtitle

# Description and image
st.write("This page is used to describe my titanic-neural-network notebook. Look below for a summary of my notebook.")
st.image("https://www.druva.com/content/dam/druvaincprogram/blog/thumbnails/blog-understanding-neural-networks-through-visualization-post.jpg", caption="Neural Network Visualization")  # Replace with your actual image path

# Additional content should be added here, replicating the structure of your HTML
# ...

# Footer or additional information
# ...

# Make sure to replace placeholder text, URLs, and paths with your actual content
