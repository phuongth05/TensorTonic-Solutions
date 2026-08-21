import numpy as np

def bottleneck_block(x, W1, W2, W3, Ws):
    """
    Returns: np.ndarray with bottleneck residual block output (compress, process, expand + skip)
    """
    # YOUR CODE HERE
    x = np.array(x)
    W1 = np.array(W1)
    W2 = np.array(W2)
    W3 = np.array(W3)
    

    if Ws is None:
        shortcut = x
    else:
        Ws = np.array(Ws)
        shortcut = x @ Ws

    return np.maximum(np.maximum(np.maximum(x @ W1, 0) @ W2, 0) @ W3 + shortcut, 0)
    pass
