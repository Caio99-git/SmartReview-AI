from transformers import pipeline

# Load a pre-trained sentiment analysis pipeline from Hugging Face
# This pipeline automatically downloads and sets up a model that can classify text as positive or negative sentiment
sentiment_classifier = pipeline("sentiment-analysis")

# Analyze sentiment of a given text ---
def get_sentiment(text):
    if len(text.strip()) == 0:
        return "Please enter some text to analyze."
        # Return message if input is empty or just spaces

    try:
        result = sentiment_classifier(text)  
        # Run sentiment analysis on the text

        label = result[0]['label']  
        score = round(result[0]['score'] * 100, 2)  # 
        # Extract label (e.g., POSITIVE/NEGATIVE) and confidence score % and round it to two decimal places

        return f"{label} ({score}%)"  
        # Return a formatted string with label and score
    except Exception as e:
        return f"Error during sentiment analysis: {e}"  
        # Return error message if something goes wrong

