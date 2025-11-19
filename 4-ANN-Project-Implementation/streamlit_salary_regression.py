import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
import tensorflow as tf
import pickle

## Load th trained model
model = tf.keras.models.load_model('salary_regression_model.h5')


# Laod the encoder and scaler
with open('label_encoder_gender.pkl', 'rb') as f:
    label_encoder_gender = pickle.load(f)
    
with open('onehot_encoder_geography.pkl', 'rb') as f:
    onehot_encoder_geography = pickle.load(f)
    
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
    
    
## Streamlit App
st.title('Salary Prediction App')

## User inputs
geography = st.selectbox('Geography', onehot_encoder_geography.categories_[0])
gender = st.selectbox("Gender", label_encoder_gender.classes_)
age = st.number_input("Age", min_value=18, max_value=100, value=30)
tenure = st.number_input("Tenure (years at company)", min_value=0, max_value=40, value=5)
balance = st.number_input("Account Balance", min_value=0, value=50000)
num_of_products = st.number_input("Number of Products", min_value=1, max_value=10, value=2)
has_cr_card = st.selectbox("Has Credit Card", [0, 1])
is_active_member = st.selectbox("Is Active Member", [0, 1])
exited = st.selectbox("Exited", [0, 1])
credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=600)


## Prepare the input data
input_data = pd.DataFrame({
    "CreditScore": [credit_score],
    "Gender" : [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    "Tenure": [tenure],
    "Balance": [balance],
    "NumOfProducts": [num_of_products],
    "HasCrCard": [has_cr_card],
    "IsActiveMember": [is_active_member],
    'Exited' : [exited]
})

## One hot encode Geography
geography_encoded = onehot_encoder_geography.transform([[geography]]).toarray()
geography_encoded_df = pd.DataFrame(geography_encoded, columns=onehot_encoder_geography.get_feature_names_out(['Geography']))

## Combine one-hot encoded columns with input data
input_data = pd.concat([input_data.reset_index(drop=True), geography_encoded_df], axis=1)

## Scale the input data
input_data_scaled = scaler.transform(input_data)

## Predict the salary
prediction = model.predict(input_data_scaled)
predicted_salary = prediction[0][0]


st.write(f'The predicted Salary: ${predicted_salary:,.2f}')

                       