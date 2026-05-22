import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here

    v = np.asarray(v)

    if v.ndim == 1:
        _norm = np.linalg.norm(v)
        if _norm <= 1e-10:
            return np.zeros_like(v)
        return v/_norm
    else:
        _norm = np.linalg.norm(v, axis=1, keepdims=True)
        _norm = np.where(_norm<= 1e-10, 1.0, _norm)
        result = v/_norm
        result[_norm.squeeze() <= 1e-10] = 0.0
        return result
    pass