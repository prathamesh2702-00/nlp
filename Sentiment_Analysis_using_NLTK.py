# Assignment 8: Sentiment Analysis using NLTK

# Import required libraries
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required resource (run once)
nltk.download('vader_lexicon')

print("----- Sentiment Analysis using VADER -----\n")

# Sample sentences
sentences = [
    "I love this product, it is absolutely amazing!",
    "The movie was okay, nothing special.",
    "I am very disappointed with the service.",
    "The weather is pleasant today.",
    "This is the worst experience of my life."
]

# Initialize VADER Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Analyze each sentence
for sentence in sentences:
    scores = sia.polarity_scores(sentence)
    compound_score = scores['compound']

    # Classification based on compound score
    if compound_score >= 0.05:
        sentiment = "Positive"
    elif compound_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(f"Sentence: {sentence}")
    print(f"Sentiment Score: {scores}")
    print(f"Predicted Sentiment: {sentiment}")
    print("-------------------------------")