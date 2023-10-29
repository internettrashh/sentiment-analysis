import streamlit as st
from gradio_client import Client
import json

st.title("Sentiment Analysis with 🤗 x Gradio x streamlit ")

# Input text box for user input
user_input = st.text_area("Enter text for sentiment analysis 🔥🔥🔥")

# gradio client ka api end point from hugging face spaces
gradio_client = Client("https://internettrashh-sentiment-analysis.hf.space/--replicas/tqf57/")


# Function to make the API call
def analyze_sentiment(input_text):
    result = gradio_client.predict(
        input_text,
        api_name="/predict"
    )
    try:
        
        result = result.replace("'", "\"")
        result = json.loads(result)
    except json.JSONDecodeError as e:
        st.error(f"Error decoding JSON: {e}")
        st.error(f"Result: {result}")
        return None, None
    label = result[0]['label']
    score = result[0]['score']
    return label, score  

if st.button("Analyze Sentiment"):
    if user_input:
        label, score = analyze_sentiment(user_input)
        if label is not None and score is not None:
            st.subheader("Analysis Result:")
            st.text(f"Sentiment👉: {label}")
            st.text(f"Score🫠: {score}")


    st.subheader("Check out the GitHub repo for the source code and more info about this project👇")
    st.markdown("[GitHub](https://github.com/internettrashh/sentiment-analysis)")
