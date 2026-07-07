import numpy as np
from collections import Counter

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here

    predictions = np.array(predictions)
    output = []

    for i in range(predictions.T.shape[0]):
        frequences = Counter(predictions.T[i])
        max_cls = max(frequences.values())
        winner = [key for key, value in frequences.items() if value == max_cls]

        output.append(min(winner))
    return output
        