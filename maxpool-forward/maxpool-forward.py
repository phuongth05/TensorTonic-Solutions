import numpy as np

def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    """
    # Write code here

    X = np.array(X)

    out_h = (X.shape[0] - pool_size) // stride + 1
    out_w = (X.shape[1] - pool_size) // stride + 1

    output = np.zeros((out_h, out_w), dtype=float)

    for i in range(out_h):
        for j in range(out_w):
            output[i, j] = np.max(X[i*stride: i*stride + pool_size, 
                            j*stride: j*stride + pool_size])

    return output.tolist()