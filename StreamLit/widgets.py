import streamlit as st
import pandas as pd
import numpy as np


st.title("streamLit Text Input")

name = st.text_input("Write your name please")

age = st.slider("Select your age:", 0, 100, 25)

st.write(f"Your age is: {age}")

options = ['python', 'java','jsvascript', 'c++']
choice= st.selectbox("Choose your fav language:",options)
st.write(f"You selected: {choice}")

if name:
    st.write(f"Hello, {name}")

data = {
    "Name":["John","Rimsha", "Kate"],
    "Age": [23,44,32],
    "City": ["Lahore","Sialkot","Karachi"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file:", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)