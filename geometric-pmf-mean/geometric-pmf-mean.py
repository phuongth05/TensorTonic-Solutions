import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    k = np.array(k)

    pmf = np.array([(1 - p)**(single_k - 1) * p for single_k in k])

    E = 1/p

    return pmf, E
    pass