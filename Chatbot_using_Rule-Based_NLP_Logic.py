# Assignment 10: Chatbot using Rule-Based NLP Logic

# Import required libraries
import nltk
from nltk.tokenize import word_tokenize

# Download required resource (run once)
nltk.download('punkt')

print("----- Rule-Based Chatbot -----\n")
print("Type 'bye' to exit the chatbot.\n")

# Predefined responses
responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! Nice to meet you.",
    "hey": "Hey! What can I do for you?",
    "how are you": "I am fine, thank you!",
    "what is your name": "I am a simple NLP chatbot.",
    "who created you": "I was created using Python and NLTK.",
    "bye": "Goodbye! Have a nice day."
}

while True:
    user_input = input("You: ").lower()

    # Tokenization
    words = word_tokenize(user_input)

    reply = "Sorry, I do not understand that."

    # Pattern matching
    if "hello" in words or "hi" in words or "hey" in words:
        reply = responses["hello"]

    elif "how" in words and "you" in words:
        reply = responses["how are you"]

    elif "name" in words:
        reply = responses["what is your name"]

    elif "created" in words:
        reply = responses["who created you"]

    elif "bye" in words:
        reply = responses["bye"]
        print("Bot:", reply)
        break

    print("Bot:", reply)