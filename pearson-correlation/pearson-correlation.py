import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    # Write code here

    X = np.array(X)

    center = X - np.mean(X, axis=0, keepdims=True)

    corr_mar = 1/(X.shape[0] - 1) * (center.T @ center)

    std = np.std(X, axis=0, ddof=1)
    denominator_mar = np.outer(std, std)

    return corr_mar/denominator_mar
    pass