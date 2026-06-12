import numpy as np

def batch_generator(X, y, batch_size, rng=None, drop_last=False):
    """
    Randomly shuffle a dataset and yield mini-batches (X_batch, y_batch).
    """
    # Write code here

    X = np.array(X)
    y = np.array(y)
    n = len(X)

    idx_arr = np.arange(n)

    if rng == None:
        np.random.shuffle(idx_arr)
    else:
        rng.shuffle(idx_arr)

    X_shuffled = X[idx_arr]
    y_shuffled = y[idx_arr]
    i = 0
    while i < n:
        yield (X_shuffled[i : i + batch_size]), (y_shuffled[i : i + batch_size])
        i += batch_size

        if drop_last and (i + batch_size) > n:
            break
    pass