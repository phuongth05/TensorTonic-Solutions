import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here

    A = np.array(A)

    if (A.ndim != 2) or (A.shape[0] != A.shape[1]):
        return None

    detA = np.linalg.det(A)

    if np.abs(detA) < 1e-10:
        return None

    return np.linalg.inv(A)
    pass
