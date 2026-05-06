
import nltk
import spacy
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag

# Download NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Load spaCy English model (install using: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

# Input paragraph
text = """Natural Language Processing (NLP) is a field of Artificial Intelligence.
It helps computers understand human language.
NLP is used in chatbots, translation systems, and sentiment analysis."""

print("Original Text:\n")
print(text)

# -------------------------------
# Using NLTK
# -------------------------------

print("\n----- Using NLTK -----\n")

# Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentence Tokenization:")
for i, sentence in enumerate(sentences, 1):
    print(f"{i}. {sentence}")

# Word Tokenization
words = word_tokenize(text)
print("\nWord Tokenization:")
print(words)

# POS Tagging
pos_tags = pos_tag(words)
print("\nPOS Tagging:")
print(pos_tags)

# -------------------------------
# Using spaCy
# -------------------------------

print("\n----- Using spaCy -----\n")

doc = nlp(text)

# Sentence Tokenization
print("Sentence Tokenization:")
for i, sent in enumerate(doc.sents, 1):
    print(f"{i}. {sent}")

# Word Tokenization + POS Tagging
print("\nWord Tokenization and POS Tagging:")
for token in doc:
    print(f"{token.text} --> {token.pos_}")