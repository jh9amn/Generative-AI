import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


## Loat the LSTM Model
model = load_model('next_word_lstm.h5')

## Loat the tokenizer
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
    
    
## Function to predict the next word
def predict_next_word(model, tokenizer, text, max_sequence_len):
    # Convert input text to tokens
    token_list = tokenizer.texts_to_sequences([text])[0]

    # Limit length to max_sequence_len - 1
    if len(token_list) >= max_sequence_len:
        token_list = token_list[-(max_sequence_len-1):]

    # Pad the input
    token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')

    # Predict probabilities
    predicted = model.predict(token_list, verbose=0)

    # Get index of highest probability
    predicted_index = np.argmax(predicted, axis=1)[0]

    # Find the corresponding word
    for word, index in tokenizer.word_index.items():
        if index == predicted_index:
            return word
    
    return None


## Streamlit APP
st.title("Next word prediction with LSTM RNN and Early Stopping")
input_text = st.text_input("Enter the sequence of words", "To be or not to")
if st.button("Predict Next Word"):
    max_sequence_len = model.input_shape[1] + 1     ## Retrieve the max sequence length from the model input shape
    next_word = predict_next_word(model, tokenizer, input_text, max_sequence_len)
    st.write(f'Next word: {next_word}')