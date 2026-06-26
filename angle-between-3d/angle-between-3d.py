import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    v = np.array(v)
    w = np.array(w)

    v_norm = np.linalg.norm(v)
    w_norm = np.linalg.norm(w)
    
    if v_norm < 10e-10 or w_norm < 10e-10:
        return np.nan
    
    cos = np.dot(v, w)/(v_norm*w_norm)

    return np.arccos(np.clip(cos, -1, 1))
    pass