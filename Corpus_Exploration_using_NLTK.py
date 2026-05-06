# Assignment 3: Corpus Exploration using NLTK

# Import required libraries
import nltk
from nltk.corpus import brown
from nltk import FreqDist

# Download Brown corpus (run once)
nltk.download('brown')

print("----- Corpus Exploration using Brown Corpus -----\n")

# Display corpus categories
print("Corpus Categories:\n")
print(brown.categories())

# Display total number of words
words = brown.words()
print("\nTotal Number of Words:")
print(len(words))

# Word Frequency Distribution
freq_dist = FreqDist(words)

print("\nMost Common 10 Words:\n")
for word, frequency in freq_dist.most_common(10):
    print(f"{word} : {frequency}")

# Display sample sentences
print("\nSample Sentences from Brown Corpus:\n")

sentences = brown.sents()

for i in range(5):
    print(f"Sentence {i+1}: {' '.join(sentences[i])}")