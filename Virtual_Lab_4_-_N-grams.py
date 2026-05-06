# Assignment 13: Virtual Lab 4 - N-grams

import nltk
from nltk.tokenize import word_tokenize
from nltk.util import bigrams, trigrams
from collections import Counter

# Download required resource (run once)
nltk.download('punkt')

print("----- Virtual Lab 4 : N-Grams -----\n")

# Input sentence
text = "Natural language processing improves human computer interaction"

print("Original Sentence:\n")
print(text)

# Tokenization
words = word_tokenize(text.lower())

print("\nTokenized Words:\n")
print(words)

# Generate Bigrams and Trigrams
bigram_list = list(bigrams(words))
trigram_list = list(trigrams(words))

print("\nBigrams:\n")
print(bigram_list)

print("\nTrigrams:\n")
print(trigram_list)

# Frequency count
bigram_freq = Counter(bigram_list)
trigram_freq = Counter(trigram_list)

print("\nBigram Frequency:\n")
print(bigram_freq)

print("\nTrigram Frequency:\n")
print(trigram_freq)

# Probability Calculation
print("\nBigram Probabilities:\n")

for bg in bigram_freq:
    first_word_count = words.count(bg[0])
    probability = bigram_freq[bg] / first_word_count
    print(f"P({bg[1]} | {bg[0]}) = {probability:.2f}")

print("\nTrigram Probabilities:\n")

for tg in trigram_freq:
    first_two_count = bigram_list.count((tg[0], tg[1]))
    probability = trigram_freq[tg] / first_two_count
    print(f"P({tg[2]} | {tg[0]}, {tg[1]}) = {probability:.2f}")