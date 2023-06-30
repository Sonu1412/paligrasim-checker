import re
import string
from collections import Counter
import math

def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation and numbers
    text = re.sub('[' + string.punctuation + '0-9]', '', text)

    # Split the text into words
    words = text.split()

    # Count the frequency of each word
    word_counts = Counter(words)

    return word_counts

def cosine_similarity(doc1, doc2):
    # Preprocess the documents
    word_counts1 = preprocess_text(doc1)
    word_counts2 = preprocess_text(doc2)

    # Get the unique words from both documents
    words = set(list(word_counts1.keys()) + list(word_counts2.keys()))

    # Calculate the dot product and the magnitudes of each document
    dot_product = sum(word_counts1.get(word, 0) * word_counts2.get(word, 0) for word in words)
    magnitude1 = math.sqrt(sum(count**2 for count in word_counts1.values()))
    magnitude2 = math.sqrt(sum(count**2 for count in word_counts2.values()))

    # Calculate the cosine similarity
    similarity = dot_product / (magnitude1 * magnitude2)

    return similarity

# Example usage
document1 = "This is the first document."
document2 = "This document is the second document."
document3 = "This is a completely different document."

similarity1 = cosine_similarity(document1, document2)
similarity2 = cosine_similarity(document1, document3)

print(f"Similarity between document 1 and document 2: {similarity1}")
print(f"Similarity between document 1 and document 3: {similarity2}")
