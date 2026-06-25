import numpy as np

def stratified_split(X, y, test_size=0.2, rng=None):
    """
    Split features X and labels y into train/test while preserving class proportions.
    """
    # Write code here
    X = np.array(X)
    y = np.array(y)

    if rng == None:
        rng = np.random.shuffle()

    classes = np.unique(y)

    test_indices, train_indices = [], []

    for cls in classes:
        indices = np.where(y == cls)[0]
        rng.shuffle(indices)
        
        samples = len(indices)
        test_samples = round(samples * test_size)

        test_idx = indices[:test_samples]
        train_idx = indices[test_samples:]

        test_indices.extend(test_idx)
        train_indices.extend(train_idx)

    X_train = X[np.sort(train_indices)]
    y_train = y[np.sort(train_indices)]
    X_test = X[np.sort(test_indices)]
    y_test = y[np.sort(test_indices)]

    return (X_train, X_test, y_train, y_test)
        
        
        

    
    pass