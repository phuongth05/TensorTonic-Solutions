import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.array(X, dtype=float)
    
    min = np.min(X, axis=axis, keepdims=True)
    max = np.max(X, axis=axis, keepdims=True)

    _X = (X-min)/np.maximum((max-min), eps)

    return _X
    
    pass