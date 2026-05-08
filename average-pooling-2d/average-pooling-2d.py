import numpy as np
def average_pooling_2d(X, pool_size):
    """
    Apply 2D average pooling with non-overlapping windows.
    """
    # Write code here

    X = np.array(X)
    H = X.shape[0]
    W = X.shape[1]

    out_h = H // pool_size
    out_w = W // pool_size

    output = np.zeros((out_h, out_w))

    for i in range(out_h):
        for j in range(out_w):
            #sum trùng
            pool_sum = 0
            for k in range(pool_size):
                for l in range(pool_size):
                    pool_sum += X[i*pool_size + k, j*pool_size + l]

            output[i, j] = pool_sum/(pool_size**2)

    return output.tolist()