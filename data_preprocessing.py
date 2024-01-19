import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import random
import tensorflow as tf
import numpy as np
import os
import joblib


# Set Global random seed to make sure we can replicate any model that we create (no randomness)
np.random.seed(42)
random.seed(42)
np.random.seed(42)
tf.random.set_seed(42)

os.environ['TF_DETERMINISTIC_OPS'] = '1'


def data_preprocessing(Pclass, Sex, Fare, Age, Sibsp, Parch):
    # Create a dictionary where keys are column names and values are data
    data = {'Pclass': [Pclass], 'Sex': [Sex], 'Fare': [Fare], 'Age': [Age], 'SibSp': [Sibsp], 'Parch': [Parch]}
    
    # Create a DataFrame from the dictionary
    train_X = pd.DataFrame(data)

    # One hot encoding
    train_X = pd.get_dummies(train_X)

    # Feature engineering

    #Create a FemaleFirstClass and ChildFirstClass feature into each dataset
    if 'Sex_female' in train_X.columns:
        train_X['FemaleFirstClass'] = ((train_X['Sex_female'] == True) & (train_X['Pclass'] == 1)).astype(int)
        train_X['Sex_male'] = 0
    else:
        train_X['FemaleFirstClass'] = 0
        train_X['Sex_female'] = 0

    #Create FamilySize and IsAlone
    train_X['FamilySize'] = train_X['SibSp'] + train_X['Parch'] + 1
    
    train_X['IsAlone'] = (train_X['FamilySize'] == 1).astype(int)
    

    # NORMALIZE THE DATA

    # Load the scaler from the original neural network notebook
    scaler = joblib.load('C:\Kaggle Machine Learning\Titanic_StreamLit_Website\scaler2.pkl')

    columns_to_normalize = ["Pclass", "Fare","Age", "SibSp"]

    train_X[columns_to_normalize] = scaler.transform(train_X[columns_to_normalize])

    user_input_normalized = train_X

    # Get it ready to be fed into TensorFlow 
    user_input_normalized = user_input_normalized.astype('float32')

    print(user_input_normalized)

    return user_input_normalized
# Index(['Pclass', 'Fare', 'Age', 'SibSp', 'Parch', 'Sex_female', 'Sex_male',
#        'FemaleFirstClass', 'FamilySize', 'IsAlone'],
#       dtype='object')




data_preprocessing(1, "male", 20, 40, 1, 2)