import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/api/sentiment"


st.title("Sentiment Analysis App")
st.write("Enter a sentence to analyze its sentiment.")
text = st.text_input("Your sentence here:")

if st.button("Analyze"):
    # Call the sentiment analysis model
    try:

        response = requests.post(API_URL, json={"sentence": text}, timeout=10)
        if response.status_code == 200:
            result = response.json()
            # st.write(result)
            label = result['label']
            confidence = result['confidence']
            sentence = result['sentence']
            st.write(f"The sentiment of the sentence is: {label}")
            st.write(f"Confidence: {confidence:.2f}%")
            st.write(f"Sentence: {sentence}")
        else:
            st.error(f"API returned an error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to the API: {e}")
    except ValueError:
        st.error("Error processing the response from the API.")