import numpy as np

def _sigmoid(x):
    """Numerically stable sigmoid function"""
    return np.where(x >= 0, 1.0/(1.0+np.exp(-x)), np.exp(x)/(1.0+np.exp(x)))

def _as2d(a, feat):
    """Convert 1D array to 2D and track if conversion happened"""
    a = np.asarray(a, dtype=float)
    if a.ndim == 1:
        return a.reshape(1, feat), True
    return a, False

def gru_cell_forward(x, h_prev, params):
    """
    Implement the GRU forward pass for one time step.
    Supports shapes (D,) & (H,) or (N,D) & (N,H).
    """
    # Write code here

    Wz = params["Wz"]
    Uz = params["Uz"]
    bz = params["bz"]
    Wr = params["Wr"]
    Ur = params["Ur"]
    br = params["br"]
    Wh = params["Wh"]
    Uh = params["Uh"]
    bh = params["bh"]
        
    x, _ = _as2d(x, Wz.shape[0])
    h_prev, _ = _as2d(h_prev, Wz.shape[1])

    z_t = _sigmoid(x @ Wz + h_prev @ Uz + bz)
    r_t = _sigmoid(x @ Wr + h_prev @ Ur + br)
    h_t = np.tanh(x @ Wh + (r_t * h_prev) @ Uh + bh)

    output = (1 - z_t) * h_prev + z_t * h_t

    if _ == True:
        output = np.squeeze(output)

    return output
    
    pass
    