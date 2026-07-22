import math
import numpy as np

def ndcg(relevance_scores, k):
    """
    Compute NDCG@k.
    """
    # Write code here

    relevance_scores = np.array(relevance_scores)
    if k > len(relevance_scores):
        k = len(relevance_scores)

    DCG = np.sum([(2**relevance_scores[i] - 1)/np.log2(i + 2) for i in range(k)])

    ideal_rel = sorted(relevance_scores, reverse=True)
    IDCG = np.sum([(2**ideal_rel[i] - 1)/np.log2(i + 2) for i in range(k)])

    return DCG/IDCG if IDCG != 0 else 0.0
    
    pass