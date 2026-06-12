import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    # Load the sentiment analysis model
    model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    return model

classifier = load_model()

st.title("Sentiment Analysis App")
st.write("Enter a sentence to analyze its sentiment.")
text = st.text_input("Your sentence here:")

if st.button("Analyze"):
    # Call the sentiment analysis model
    result = classifier(text)
    # st.write(result)
    sentiment = result[0]['label']
    confidence = result[0]['score'] * 100
    st.write(f"The sentiment of the sentence is: {sentiment}")
    st.write(f"Confidence: {confidence:.2f}%")