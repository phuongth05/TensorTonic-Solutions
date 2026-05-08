import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    # Write code here

    N = len(documents)
    documents = [document.lower().split() for document in documents]

    vocabulary = set(term for document in documents
                          for term in document)

    vocabulary = sorted(vocabulary)
    
    tfidf_matrix = np.zeros((N, len(vocabulary)), dtype=float)

    word_2_idx = {word : idx
                 for idx, word in enumerate(vocabulary)}

    for i, document in enumerate(documents):
        document_cnt = Counter(document)
        for term in document:
            tf = document_cnt[term] / len(document)

            df = sum(term in document for document in documents)
            idf = math.log(N / df)
            
            tf_idf = tf * idf

            tfidf_matrix[i, word_2_idx[term]] = tf_idf

    return tfidf_matrix, vocabulary
    pass