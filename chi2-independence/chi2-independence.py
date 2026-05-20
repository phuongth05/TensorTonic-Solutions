import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here

    C = np.array(C, dtype=float)

    row_sum = np.sum(C, axis=1, keepdims=False)
    col_sum = np.sum(C, axis=0, keepdims=False)
    total = np.sum(row_sum, keepdims=False)

    E = np.outer(row_sum, col_sum)/total

    X_square = np.sum((C - E)**2/E)

    return X_square, E
    pass