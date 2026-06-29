import numpy as np

def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    # Write code here

    x = np.array(x)

    if x.ndim not in [3, 4]:
        raise ValueError
    W = x.shape[-1]
    H = x.shape[-2]

    return 1/(H*W) * np.sum(np.sum(x, axis=-1),axis=-1) if (H>=1 and W>=1) else 0.0
    pass