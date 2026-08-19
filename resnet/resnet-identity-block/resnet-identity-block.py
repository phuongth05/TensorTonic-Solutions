import numpy as np

def identity_block(x, W1, W2):
    """
    Returns: np.ndarray of shape (batch, channels) with identity residual block output
    """
    # YOUR CODE HERE

    x = np.array(x)
    W1 = np.array(W1)
    W2 = np.array(W2)

    h = np.maximum(x @ W1.T, 0)

    return np.maximum(h @ W2.T + x, 0)
    pass
