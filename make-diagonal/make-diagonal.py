import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here

    v = np.array(v)

    output = np.zeros((v.shape[0], v.shape[0]))

    for i in range(v.shape[0]):
        output[i][i] = v[i]

    return output
    pass
