import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")

## Lets create a slider widget
age = st.slider("select your age:", 0, 100, 25)
st.write(f"You are {age} years old.")

## Lets create a selectbox widget
options = ["Python", "Java", "C++", "JavaScript"]
lang_choice = st.selectbox("Select your favorite programming language:", options)
st.write(f"You selected: {lang_choice}")

if name:
    st.write(f"Hello, {name}!")

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Chooss as CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)