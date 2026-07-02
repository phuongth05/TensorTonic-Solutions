def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    # Write code here

    pair = []

    for i, score in enumerate(scores):
        if i not in rated_indices:
            pair.append((score, i))

    pair_sorted = sorted(pair, key=lambda x: -x[0])

    result = [x[1] for x in pair_sorted]

    return result[:k]