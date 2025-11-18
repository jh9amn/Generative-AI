## Step 1:  Import libaries and Load the Model
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence
import streamlit as st
from tensorflow.keras.datasets import imdb




## Laod the IMDB word index
word_index = imdb.get_word_index()
reverse_word_index = {value: key  for (key, value) in word_index.items()}

## Load the pretrainned model with ReLU activation
model = load_model('simplernn_imdb_model.h5')


## Step 2: preprocess the user input
def decode_review(encode_review):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encode_review])

## Funtion to preprocess the user input
def preprocess_text(review, maxLen=500, num_words=10000):
    # Tokenize the review based on the IMDB word index
    tokens = []
    for word in review.split():
        index = word_index.get(word.lower(), 2)  # 2 is for unknown words
        
         # Clip words outside model's vocabulary
        if index >= num_words:
            index = 2  # treat as unknown
        
        tokens.append(index + 3)  # Offset by 3 for special tokens

    # Pad the sequence to the maximum length
    padded_sequence = sequence.pad_sequences([tokens], maxlen=maxLen)
    return padded_sequence

## Step 3: Define prediction function
# def predict_sentiment(review):
#     preprocessed_review = preprocess_text(review)
#     prediction = model.predict(preprocessed_review)
#     sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'
    
#     return sentiment, prediction[0][0]



## Step 4: Streamlit Web App Interface
st.title("Movie Review Sentiment Prediction with SimpleRNN")
st.write("Enter a movie review below to predict its sentiment (Positive/Negative).")

## User input text area
user_review = st.text_area("Movie Review", "Type your review here...")  


if st.button("Predict Sentiment"):
    if len(user_review.strip()) == 0:
            st.write("Please enter a valid movie review.")
    else:
        processed = preprocess_text(user_review)
        prediction = model.predict(processed)
        sentiment = "Positive" if prediction[0][0] > 0.5 else "Negative"

        st.write(f"Predicted Sentiment: **{sentiment}**")
        st.write(f"Prediction Score: **{prediction[0][0]:.4f}**")   
    
else:
    st.write("Please enter a movie review and click the 'Predict Sentiment' button.")
