import numpy as np
import math

def adjusted_cosine_similarity(ratings_matrix, item_i, item_j):
    """
    Compute adjusted cosine similarity between two items.
    """
    # Write code here

    rating = np.array(ratings_matrix, dtype=float)

    num = 0.0
    sum_i = 0.0
    sum_j = 0.0

    den = 0.0

    for user in rating:
        if user[item_i] != 0 and user[item_j] != 0:
            nonzero_mask = np.where(user != 0)[0]
            r_mean = np.mean(user[nonzero_mask])

            sum_i += (user[item_i] - r_mean)**2
            sum_j += (user[item_j] - r_mean)**2

            num += (user[item_i] - r_mean) * (user[item_j] - r_mean)

    den += math.sqrt(sum_i) * math.sqrt(sum_j)

    if den == 0:
        return 0.0
                
    return num/den