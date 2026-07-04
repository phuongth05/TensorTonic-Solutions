import numpy as np

def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here
    items = np.array(items)
    
    v = len(items)
    R = []

    for i in range(v):
        num_votes = items[i, 1]
        avg_rating = items[i, 0]
        R.append((num_votes / (num_votes + min_votes)) * avg_rating + (min_votes / (num_votes + min_votes)) * global_mean)

    return R