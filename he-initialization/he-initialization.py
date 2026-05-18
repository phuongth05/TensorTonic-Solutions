import numpy as np
def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here
    W = np.array(W, dtype=float)
    r = W.shape[0]
    c = W.shape[1]
    
    L = math.sqrt(6 / fan_in)
    

    for i in range(r):
        for j in range(c):
            W[i, j] = W[i, j] * 2 * L - L

    return W.tolist()