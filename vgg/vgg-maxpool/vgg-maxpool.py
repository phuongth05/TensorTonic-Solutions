import numpy as np

def vgg_maxpool(x: np.ndarray) -> np.ndarray:
    """
    Implement VGG-style max pooling (2x2, stride 2).
    """
    # Your implementation here

    N, H, W, C = x.shape

    H_out = H // 2
    W_out = W // 2

    out = np.zeros((N, H_out, W_out, C), dtype=float)

    for h in range(H_out):
        for w in range(W_out):
            for n in range(N):
                for c in range(C):
                    out[n, h, w, c] = np.max((x[n,2*h,2*w,c],x[n,2*h,2*w+1,c],x[n,2*h+1,2*w,c],x[n,2*h+1,2*w+1,c]))

    return out
    pass