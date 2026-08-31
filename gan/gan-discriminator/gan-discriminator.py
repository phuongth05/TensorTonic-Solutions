import numpy as np

def discriminator(x, W):
    """
    Returns: np.ndarray of shape (batch, 1) with probabilities rounded to 4 decimals
    """
    x = np.array(x)
    W = np.array(W)
    return 1/(1 + np.exp(- x @ W))
    pass