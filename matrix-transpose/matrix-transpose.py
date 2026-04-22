import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code 
    A = np.array(A)
    m, n = A.shape
    A_transpose = np.zeros((n, m))

    for i in range(n):
        for j in range(m):
            A_transpose[i][j] = A[j][i]

    return A_transpose
    
    pass
