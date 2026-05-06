# Assignment 9: Keyword Extraction using spaCy

# Import required libraries
import spacy
from collections import Counter

# Load English model
# Install using: python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")

print("----- Keyword Extraction using spaCy -----\n")

# Input document
text = """
Natural Language Processing is a branch of Artificial Intelligence.
It helps computers understand human language and perform tasks like translation,
chatbots, speech recognition, and sentiment analysis.
Machine learning improves the efficiency of NLP systems.
"""

print("Original Document:\n")
print(text)

# Process text using spaCy
doc = nlp(text)

# Extract nouns only
nouns = []

for token in doc:
    if token.pos_ == "NOUN" or token.pos_ == "PROPN":
        nouns.append(token.text.lower())

# Extract noun phrases
noun_phrases = []

for chunk in doc.noun_chunks:
    noun_phrases.append(chunk.text.lower())

# Count frequency
noun_freq = Counter(nouns)
phrase_freq = Counter(noun_phrases)

# Display top keywords
print("\nTop Nouns:\n")
for word, freq in noun_freq.most_common(10):
    print(f"{word} : {freq}")

print("\nTop Noun Phrases:\n")
for phrase, freq in phrase_freq.most_common(10):
    print(f"{phrase} : {freq}")