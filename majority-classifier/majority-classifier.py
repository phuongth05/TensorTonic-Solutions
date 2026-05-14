import numpy as np
from collections import Counter

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here

    cnt = Counter(y_train)
    max_cnt_y = cnt.most_common(1)[0][0]

    result = [max_cnt_y] * len(X_test)

    return result
    pass