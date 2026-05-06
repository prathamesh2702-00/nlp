# Assignment 6: Stemming vs Lemmatization Comparison

# Import required libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer, WordNetLemmatizer

# Download required resources (run once)
nltk.download('punkt')
nltk.download('wordnet')

print("----- Stemming vs Lemmatization Comparison -----\n")

# Sample sentence
text = "The children are playing happily in the gardens and running faster."

print("Original Sentence:\n")
print(text)

# Tokenization
words = word_tokenize(text.lower())

# Remove punctuation
words = [word for word in words if word.isalpha()]

print("\nTokenized Words:\n")
print(words)

# Porter Stemmer
porter = PorterStemmer()
porter_result = [porter.stem(word) for word in words]

print("\nPorter Stemmer Output:\n")
print(porter_result)

# Snowball Stemmer
snowball = SnowballStemmer("english")
snowball_result = [snowball.stem(word) for word in words]

print("\nSnowball Stemmer Output:\n")
print(snowball_result)

# WordNet Lemmatizer
lemmatizer = WordNetLemmatizer()
lemma_result = [lemmatizer.lemmatize(word) for word in words]

print("\nWordNet Lemmatizer Output:\n")
print(lemma_result)