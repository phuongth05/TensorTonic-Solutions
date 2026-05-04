import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    vocab_dict = {}

    for i in range(len(vocab)):
        vocab_dict[vocab[i]] = i

    output = np.zeros(len(vocab), dtype=int)

    for token in tokens:
        if token in vocab_dict:
            output[vocab_dict[token]] += 1

    return output
    pass