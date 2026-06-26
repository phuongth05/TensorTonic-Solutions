import numpy as np

def silhouette_score(X, labels):
    """
    Compute the mean Silhouette Score for given points and cluster labels.
    X: np.ndarray of shape (n_samples, n_features)
    labels: np.ndarray of shape (n_samples,)
    Returns: float
    """
    # Write code here

    X = np.array(X)
    labels = np.array(labels)
    n = X.shape[0]
    unique_label = np.unique(labels)
    s = np.zeros(n, dtype=float)


    distances = np.linalg.norm(X[np.newaxis, :, :] - X[:, np.newaxis, :], axis=-1)

    for i in range(n):
        cluster_mask = (labels == labels[i])

        cluster_mask[i] = False

        if np.sum(cluster_mask) > 0:
            a = np.mean(distances[i, cluster_mask])
        else:
            a = 0

        b = float('inf')
        for label in unique_label:
            if label == labels[i]:
                continue

            other_mask = (labels == label)
            b_label = np.mean(distances[i, other_mask])

            b = min(b_label, b)

        s[i] = (b - a)/(max(a, b)) if max(a, b) != 0 else 0.0

    return np.mean(s)
    pass