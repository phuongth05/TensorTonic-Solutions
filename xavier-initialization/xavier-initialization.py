import numpy as np

def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    # Write code here

    W = np.array(W, dtype=float)
    r = W.shape[0]
    c = W.shape[1]

    L = np.sqrt(6 / (fan_in + fan_out))

    for i in range(r):
        for j in range(c):
            W[i, j] = W[i, j] * 2 * L - L

    return W.tolist()