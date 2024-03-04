import streamlit as st
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load the tokenizer used during fine-tuning
tokenizer = AutoTokenizer.from_pretrained('yiyanghkust/finbert-pretrain')

# Load your saved fine-tuned model
model_path = "likith123/SSAF-FinBert"
model = AutoModelForSequenceClassification.from_pretrained(model_path)

# Define function for sentiment prediction
def predict_sentiment(input_text):
    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, padding=True, max_length=512)

    # Perform inference
    with torch.no_grad():
        outputs = model(**inputs)

    # Get predicted probabilities for each class
    predicted_probs = torch.softmax(outputs.logits, dim=1).squeeze().tolist()

    return predicted_probs

# Streamlit UI
def main():
    st.title("Stock News Sentiment Analysis")

    # Input text boxes for user input
    headline = st.text_input("Enter the news headline:")
    content = st.text_area("Enter the news content:")

    # Button to trigger prediction
    if st.button("Predict"):
        # Combine headline and content
        combined_text = headline + " " + content

        # Perform sentiment prediction
        predicted_probs = predict_sentiment(combined_text)

        # Map the predicted probabilities to sentiment labels
        label_map = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}

        # Display predicted sentiment percentages
        st.subheader("Predicted Sentiment:")
        sorted_sentiments = sorted(zip(label_map.values(), predicted_probs), key=lambda x: x[1], reverse=True)
        for sentiment_label, prob in sorted_sentiments:
            if sentiment_label == 'Positive':
                st.write(f"{sentiment_label.capitalize()} ✅:- {prob * 100:.2f}%", unsafe_allow_html=True)
            elif sentiment_label == 'Negative':
                st.write(f"{sentiment_label.capitalize()} ❌:- {prob * 100:.2f}%", unsafe_allow_html=True)
            else:
                st.write(f"{sentiment_label.capitalize()} ⏳:- {prob * 100:.2f}%", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
