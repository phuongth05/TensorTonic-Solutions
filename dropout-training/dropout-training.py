import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here

    x = np.array(x)

    if rng is None:
        rng = np.random

    random_matrix = rng.random(x.shape)

    dropout_pattern = (random_matrix < (1 - p)).astype(x.dtype)  / (1 - p)


    output = x * dropout_pattern
    return output, dropout_pattern
    pass