import numpy as np

def gini(y):
    if len(y) == 0:
        return 0
    _, counts = np.unique(y, return_counts=True)
    probs = counts / len(y)
    
    return 1 - np.sum(probs ** 2)

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Write code here
    y_left = np.array(y_left)
    y_right = np.array(y_right)

    n = len(y_left) + len(y_right)

    if n == 0:
        return 0.0

    return len(y_left)/n * gini(y_left) + len(y_right)/n * gini(y_right)
    pass