from collections import Counter

def bigram_probabilities(tokens):
    """
    Returns: (counts, probs)
      counts: dict mapping (w1, w2) -> integer count
      probs: dict mapping (w1, w2) -> float P(w2 | w1) with add-1 smoothing
    """
    # Your code here

    vocab = set(tokens)

    pairs = [(tokens[i], tokens[i + 1]) for i in range(len(tokens) - 1)]
    pair_counts = Counter(pairs)
    P = {}
    V = len(vocab)
    word_counts = Counter(tokens[:-1])

    for word_1 in vocab:
        count_wu = word_counts[word_1]

        for word_2 in vocab:
            pair_count = pair_counts[(word_1, word_2)]

            P[(word_1, word_2)] = (pair_count + 1)/(count_wu + V)

    return (dict(pair_counts), P)
    pass