import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try: 
        matrix = np.asarray(matrix)
    except ValueError:
        return None

    matt_dim = matrix.ndim

    if matt_dim < 2:
        return None

    r, c = matrix.shape
    if r != c:
        return None
    
    eigvals = np.linalg.eigvals(matrix)
    idx = np.lexsort((eigvals.imag, eigvals.real))
    eigvals = eigvals[idx]

    return eigvals
    pass