import pickle
import os
import streamlit as st
from predict import predict_sentiment

st.set_page_config(
    page_title="Sentiment Analysis",
    layout="centered"
)

st.title("Sentiment Analysis App")
st.write("Enter text to predict emotion")

text_input = st.text_area(
    "Input Text",
    placeholder="Example: I am feeling very happy today"
)

if st.button("Predict"):
    if text_input.strip() == "":
        st.warning("Please enter some text")
    else:
        try:
            prediction = predict_sentiment(text_input)
            st.success(f"Predicted Emotion: **{prediction}**")
        except Exception as e:
            st.error(f"Error: {e}")
