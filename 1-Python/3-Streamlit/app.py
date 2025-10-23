import streamlit as st
import pandas as pd
import numpy as np

# Display title
st.title("Hello Streamlit")

# Display simple text
st.write("This is my simple text")



## Create a simple Datafrmame
df = pd.DataFrame({
    'first column' : [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# Display the DataFrame
st.write("Here is the data frame")
st.write(df)

# Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=['a', 'b', 'c']
)
st.line_chart(chart_data)