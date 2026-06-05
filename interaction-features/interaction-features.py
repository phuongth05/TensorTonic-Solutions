import numpy as np
def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    # Write code here
    X = np.array(X)

    rows = X.shape[0]
    dimensions = X.shape[1]
    add_on = []
    
    
    for row in range(rows):
        interactions = []
        for i in range(dimensions - 1):
            interactions.extend([X[row, i] * X[row, j] for j in range(i + 1, dimensions)])

        add_on.append(interactions)

    add_on = np.array(add_on)

    X = np.concatenate((X, add_on), axis = 1)
    return X.tolist()