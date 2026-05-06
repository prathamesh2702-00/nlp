
# Import spaCy
import spacy

# Load English language model
# Install using: python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")

# Input news article text
text = """
Microsoft CEO Satya Nadella visited India on Monday.
He met Prime Minister Narendra Modi in New Delhi.
They discussed Artificial Intelligence, cloud computing, and future technology investments.
Microsoft also announced a new research center in Mumbai.
"""

print("Original News Article:\n")
print(text)

# Process the text using spaCy
doc = nlp(text)

print("\n----- Named Entity Recognition (NER) -----\n")

# Display named entities
for ent in doc.ents:
    print(f"Entity: {ent.text}")
    print(f"Label : {ent.label_}")
    print("---------------------------")
