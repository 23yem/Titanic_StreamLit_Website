# Introduction
The Titanic StreamLit Website is an interactive web platform showcasing machine learning models developed for the Kaggle Titanic dataset. The website features a homepage and dedicated pages for Neural Network, Random Forest, and Gradient Boosted Trees models. This project serves as a testament to the deployment of machine learning models to the cloud, leveraging Streamlit for seamless integration.

### Website Structure
1. **Home Page**: The homepage (`index.html`) introduces the project, providing a glimpse into the machine learning models used and the data preprocessing techniques. Links to GitHub repositories and other model pages are also available.

2. **Model Pages**: 
    - **Neural Network (`Neural_Network.py`)**: This page, structured with HTML (`Neural_Network_1.html` and `Neural_Network_2.html`), presents the neural network model. Users can input custom values like age and gender to receive survival predictions.
    - **Random Forest (`Random_Forest.py`)**: Similar in structure to the Neural Network page, this page (`Random_Forest_1.html` and `Random_Forest_2.html`) focuses on the Random Forest model, allowing users to interact and receive predictions.
    - **Gradient Boosted Trees (`Gradient_Boosted.py`)**: Showcasing the Gradient Boosted Trees model, this page (`Gradient_Boosted_1.html` and `Gradient_Boosted_2.html`) also allows for interactive user input and predictions.

### Technical Details
- **Data Preprocessing**: Separate preprocessing scripts for each model (`data_preprocessing_neural_network.py`, `data_preprocessing_Random_Forest.py`, `data_preprocessing_Gradient_Boosted.py`) ensure data is formatted correctly for model input.
- **Model Deployment**: Models are saved and deployed using Streamlit. For instance, `model_12_saved.h5` represents a saved neural network model, and `model3_GB/saved_model.pb` for the Gradient Boosted Trees.
- **Requirements**: The `requirements.txt` file lists all the necessary libraries and dependencies required to run the models and the website.

### Machine Learning Pipeline
- **Model Training**: Detailed training and fine-tuning of models are evident in the code and HTML descriptions, ensuring optimal performance.
- **Evaluation and Scoring**: The project boasts a high score of 80.622 in the Kaggle competition, indicating the efficacy of the models and the engineering pipeline.

### Learnings and Achievements
- This project illustrates the integration of HTML with Streamlit, displaying the capability to create interactive web applications for machine learning models.
- It highlights the deployment of models to the cloud, allowing for real-time interaction and prediction based on user input.
- The repository serves as an educational tool for understanding model deployment, cloud integration, and the use of Streamlit in machine learning projects.

### Links and References
For an in-depth view and understanding of this project, visit the [GitHub Repository](https://github.com/23yem/Titanic_StreamLit_Website) and explore the various HTML and Python files that constitute the website's structure and functionality.

