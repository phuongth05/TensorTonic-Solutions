import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here

    x = np.array(x, dtype=float)
    n = x.shape[0]

    _mean = np.mean(x)
    _var = 1/(n-1) * np.sum((x - _mean)**2)
    _std = np.sqrt(_var)

    return (_var, _std)
    pass