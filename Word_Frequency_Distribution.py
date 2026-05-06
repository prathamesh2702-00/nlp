# Assignment 4: Word Frequency Distribution

# Import required libraries
import nltk
import matplotlib.pyplot as plt
from nltk.corpus import movie_reviews
from nltk import FreqDist
from nltk.corpus import stopwords
import string

# Download required resources (run once)
nltk.download('movie_reviews')
nltk.download('stopwords')

print("----- Word Frequency Distribution using movie_reviews Corpus -----\n")

# Get all words from corpus
words = movie_reviews.words()

# Remove punctuation and stopwords
stop_words = set(stopwords.words('english'))
filtered_words = []

for word in words:
    word = word.lower()
    if word not in stop_words and word not in string.punctuation and word.isalpha():
        filtered_words.append(word)

# Frequency Distribution
freq_dist = FreqDist(filtered_words)

# Display top 20 frequent words
print("Top 20 Most Frequent Words:\n")
top_words = freq_dist.most_common(20)

for word, frequency in top_words:
    print(f"{word} : {frequency}")

# Plot graph
words_list = [word for word, freq in top_words]
freq_list = [freq for word, freq in top_words]

plt.figure(figsize=(12, 6))
plt.bar(words_list, freq_list)
plt.title("Top 20 Most Frequent Words in movie_reviews Corpus")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()