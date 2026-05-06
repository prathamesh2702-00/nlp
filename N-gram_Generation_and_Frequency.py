# Assignment 7: N-gram Generation and Frequency

# Import required libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk import FreqDist

# Download required resource (run once)
nltk.download('punkt')

print("----- N-gram Generation and Frequency -----\n")

# Input sentence
text = "Natural Language Processing helps computers understand human language"

print("Original Sentence:\n")
print(text)

# Tokenization
words = word_tokenize(text.lower())

print("\nTokenized Words:\n")
print(words)

# Generate Unigrams
unigrams = list(ngrams(words, 1))
print("\nUnigrams:\n")
print(unigrams)

# Generate Bigrams
bigrams = list(ngrams(words, 2))
print("\nBigrams:\n")
print(bigrams)

# Generate Trigrams
trigrams = list(ngrams(words, 3))
print("\nTrigrams:\n")
print(trigrams)

# Frequency Distribution

print("\n----- Frequency Distribution -----\n")

print("Unigram Frequency:")
print(FreqDist(unigrams))

print("\nBigram Frequency:")
print(FreqDist(bigrams))

print("\nTrigram Frequency:")
print(FreqDist(trigrams))