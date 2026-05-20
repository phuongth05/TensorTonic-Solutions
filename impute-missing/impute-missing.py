import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    # Write code here

    X_copy = np.array(X, dtype=float)

    if X_copy.ndim == 1:
        nan_idx = np.isnan(X_copy)
        value_idx = np.logical_not(nan_idx)

        if not np.any(value_idx):
            X_copy[nan_idx] = 0
            return X_copy

        values = X_copy[value_idx]
        
        if strategy=='mean':
            filler = np.mean(values)
        elif strategy=='median':
            filler = np.median(values)
        else:
            return X_copy

        X_copy[nan_idx] = filler

    else:
        N, D = X_copy.shape

        for c in range(D):
            nan_idx = np.isnan(X_copy[:, c])
            value_idx = np.logical_not(nan_idx)

            if not np.any(value_idx):
                X_copy[nan_idx, c] = 0
                continue

            values = X_copy[value_idx, c]

            if strategy == 'mean':
                filler = np.mean(values)
            elif strategy == 'median':
                filler = np.median(values)
            else:
                return X_copy

            X_copy[nan_idx, c] = filler

    return X_copy
    pass