def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here

    top_k = recommended[:k]
    top_k = set(top_k)
    relevant = set(relevant)

    hits = len(top_k & relevant)

    precision_k = hits/k if k > 0 else 0
    recall_k = hits/len(relevant) if len(relevant) > 0 else 0

    return [precision_k, recall_k]

    

    