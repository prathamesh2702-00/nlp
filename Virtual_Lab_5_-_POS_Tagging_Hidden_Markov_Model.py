# Assignment 14: Virtual Lab 5 - POS Tagging using Hidden Markov Model

import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download required resources (run once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

print("----- Virtual Lab 5 : POS Tagging using HMM -----\n")

# Input sentence
text = "The quick brown fox jumps over the lazy dog"

print("Original Sentence:\n")
print(text)

# Tokenization
words = word_tokenize(text)

print("\nTokenized Words:\n")
print(words)

# POS Tagging (simulating HMM-based tagging using NLTK tagger)
tagged_words = pos_tag(words)

print("\nPOS Tagged Output:\n")

for word, tag in tagged_words:
    print(f"{word} --> {tag}")

# Simple probability explanation
print("\nExample HMM Concept:\n")
print("State = POS Tag (NN, VB, JJ, etc.)")
print("Observation = Word")
print("Transition Probability = P(Tag2 | Tag1)")
print("Emission Probability = P(Word | Tag)")