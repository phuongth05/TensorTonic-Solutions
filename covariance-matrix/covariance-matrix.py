import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here

    X = np.array(X)

    if X.shape[0] < 2 or X.ndim < 2:
        return None

    _mean = np.mean(X, axis=0, keepdims=True)
    X_centered = X - _mean

    Covariance_mar = 1/(X.shape[0] - 1) * (X_centered.T @ X_centered)

    return Covariance_mar
    pass