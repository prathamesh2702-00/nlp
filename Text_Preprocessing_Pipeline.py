# Assignment 5: Text Preprocessing Pipeline

# Import required libraries
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required resources (run once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

print("----- Text Preprocessing Pipeline -----\n")

# Input paragraph
text = """
Natural Language Processing is an important field of Artificial Intelligence.
It helps computers understand, interpret, and respond to human language efficiently.
"""

print("Original Text:\n")
print(text)

# Step 1: Lowercasing
text = text.lower()
print("\nAfter Lowercasing:\n")
print(text)

# Step 2: Word Tokenization
words = word_tokenize(text)

# Step 3: Remove punctuation
words = [word for word in words if word not in string.punctuation]

print("\nAfter Punctuation Removal:\n")
print(words)

# Step 4: Remove Stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

print("\nAfter Stopword Removal:\n")
print(filtered_words)

# Step 5: Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]

print("\nAfter Stemming:\n")
print(stemmed_words)

# Step 6: Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

print("\nAfter Lemmatization:\n")
print(lemmatized_words)