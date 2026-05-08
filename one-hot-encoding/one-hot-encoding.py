import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    # Write code here

    y = np.array(y)

    if num_classes is None:
        num_classes = np.max(y) + 1

    if (np.any(y >= num_classes) or np.any(y < 0)):
        return y
        
    Y = np.zeros((len(y), num_classes), dtype=float)
    Y[np.arange(len(y)), y] = 1.0

    return Y
    pass