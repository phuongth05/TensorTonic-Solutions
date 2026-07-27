import numpy as np

def conv2d(x, W, b):
    """
    Simple 2D convolution layer forward pass.
    Valid padding, stride=1.
    """
    # Write code here

    x = np.array(x)
    W = np.array(W)
    b = np.array(b)

    N, C_in, H, W_ = x.shape
    C_out, _, KH, KW = W.shape

    H_out = H - KH + 1
    W_out = W_ - KW + 1

    y = np.zeros((N, C_out, H_out, W_out), dtype=float)

    for n in range(N):
        for cout in range(C_out):
            for h in range(H_out):
                for w in range(W_out):
                    x_slice = x[n, :, h:h+KH, w:w+KW]

                    y[n, cout, h, w] = np.sum(x_slice*W[cout]) + b[cout]

    return y
    pass