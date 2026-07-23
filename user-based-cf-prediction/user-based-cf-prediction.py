import numpy as np

def user_based_cf_prediction(similarities, ratings):
    """
    Predict a rating using user-based collaborative filtering.
    """
    # Write code here

    similarities = np.array(similarities)
    ratings = np.array(ratings)

    positive_mask = np.where(similarities > 0)[0]

    if len(positive_mask) == 0:
        return 0

    sim_positive = similarities[positive_mask]
    rat_positive = ratings[positive_mask]

    return np.sum([s * r for s, r in zip(sim_positive, rat_positive)])/np.sum(sim_positive)