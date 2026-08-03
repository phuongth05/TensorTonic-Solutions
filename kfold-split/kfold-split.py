import numpy as np

def kfold_split(N, k, shuffle=True, rng=None):
    """
    Returns: list of length k with tuples (train_idx, val_idx)
    """
    # Write code here

    result = []

    idx = np.arange(N)
    if shuffle == True:
        if rng: 
            rng.shuffle(idx)
        else:
            np.random.shuffle(idx)

    folds = np.array_split(idx, k)

    for i, fold in enumerate(folds):
        val = fold
        train = np.concatenate(folds[:i] + folds[i + 1:])
        result.append((train, val))


    return result
    pass
