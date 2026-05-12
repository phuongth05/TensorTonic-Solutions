import numpy as np

def knn_distance(X_train, X_test, k):
    """
    Compute pairwise distances and return k nearest neighbor indices.
    """
    # Write code here

    X_train = np.array(X_train)
    X_test = np.array(X_test)

    if X_train.ndim == 1:
        X_train = X_train.reshape(-1, 1)
    if X_test.ndim == 1:
        X_test = X_test.reshape(-1, 1)

    distance = np.sqrt(np.sum(((X_test[:, np.newaxis,:] - X_train[np.newaxis, :, :])**2), axis=2, keepdims=False))
    distance = np.argsort(distance, axis=1)

    if k > X_train.shape[0]:
        result = -1 * np.ones((X_test.shape[0], k), dtype=int)
        result[:, :X_train.shape[0]] = distance
        return result

    result = distance[:, :k]
    
    return result
    pass