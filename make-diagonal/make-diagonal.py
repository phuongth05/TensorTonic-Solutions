import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here

    v = np.array(v, dtype=float)
    n = v.shape[0]

    output = np.zeros((n, n), dtype=float)

    for i in range(n):
        output[i, i] = v[i]

    return output
    pass
