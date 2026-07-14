import numpy as np

def novelty_score(recommendations, item_counts, n_users):
    """
    Compute the average novelty of a recommendation list.
    """
    # Write code here

    R = len(recommendations)

    rcms = np.array(recommendations)
    counts = np.array(item_counts)

    novelty = 1/R * np.sum(- np.log2([count/n_users for count in counts]))

    return novelty