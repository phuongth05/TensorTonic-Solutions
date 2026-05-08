import numpy as np
def max_pooling_2d(X, pool_size):
    """
    Apply 2D max pooling with non-overlapping windows.
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

            max = float('-inf')
            for k in range(pool_size):
                for l in range(pool_size):
                    #i, j*pool_size = vi tri thuc cua pixel tren X
                    #+k + l la diem dang xet trong pool
                    current = X[i*pool_size + k, j*pool_size + l]
                    
                    if current > max:
                        max = current

            output[i, j] = max

    return output.tolist()