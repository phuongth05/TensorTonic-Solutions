import numpy as np
def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    # Write code here

    X = np.array(X)
    W = np.array(W)
    b = np.array(b)

    n = X.shape[0]
    d_in = W.shape[0]
    d_out = W.shape[1]
    
    Y = np.zeros((n, d_out), dtype=float)

    for i in range(n):
        for j in range(d_out):
            _sum = 0
            for k in range(d_in):
                _sum += X[i, k] * W[k, j]

            Y[i, j] = _sum + b[j]

    return Y.tolist()