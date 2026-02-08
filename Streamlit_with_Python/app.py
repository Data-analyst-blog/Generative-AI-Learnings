import streamlit as st
import pandas as pd
import numpy as np


## Title of the application
st.title("Hello Streamlit with Python")

## Display a simple text
st.write("This is my first Streamlit application!")

## Create a simple DataFrame
df = pd.DataFrame({
    'Column_A':[1,2,3,4],
    'Column_B':[10,20,30,40]
})

## Display the DataFrame
st.write("Here is a simple DataFrame:")
st.dataframe(df)

## Create a simple line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c'])
st.line_chart(chart_data)