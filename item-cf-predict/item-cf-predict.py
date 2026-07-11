import numpy as np

def item_cf_predict(user_ratings, item_similarities, target):
    """
    Predict the rating using item-based collaborative filtering.
    """
    # Write code here
    r = np.array(user_ratings)
    s = np.array(item_similarities)

    r = np.delete(r, target)
    s = np.delete(s, target)

    valid_mask = (r > 0) & (s > 0)

    valid_r = r[valid_mask]
    valid_s = s[valid_mask]

    if np.sum(valid_s) == 0:
        return 0.0

    return np.dot(valid_r, valid_s)/np.sum(valid_s)
