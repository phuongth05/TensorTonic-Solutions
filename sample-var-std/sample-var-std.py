import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.array(x)
    _mean = np.mean(x)

    var = 1/(x.shape[0]-1) * np.sum((x - _mean)**2)
    std = np.sqrt(var)
    return var, std
    pass