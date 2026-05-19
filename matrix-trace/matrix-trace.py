import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A = np.array(A, dtype=float)
    n = A.shape[0]
    sum_ = 0
    for i in range(n):
        sum_ += A[i, i]

    return sum_
    pass
