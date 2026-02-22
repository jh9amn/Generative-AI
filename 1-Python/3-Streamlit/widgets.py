import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter the name:")
if name:
    st.write(f"Hello, {name}")
    

age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is, {age}")



## Select Box
options = ["Python", "C++", "java", "javascript"]
choice = st.selectbox("Chose your favorite language:", options)
st.write(f"You selected {choice}")


## DataFrame
data = {
    "name": ["John", "Jane", "Jake", "Jill"],
    "age" : [20, 25, 28, 40],
    "city": ["New york", "Los Angeles", "Chicago", "Houston"]
}


df = pd.DataFrame(data)
df.to_csv("sample.csv")
st.write(df)



## Upload file
uploaded_file = st.file_uploader("Choose a csv file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)