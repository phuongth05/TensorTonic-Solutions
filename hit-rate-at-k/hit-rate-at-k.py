import numpy as np

def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    
    hits = 0 
    for rec, truth in zip(recommendations, ground_truth):
        if len(np.intersect1d(rec[:k], truth)) > 0:
            hits += 1

    return hits/len(ground_truth)