import numpy as np

def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    # Write code here

    n = len(values) - window_size + 1
    smas = []

    for i in range(n):
        sma = np.sum(values[i:i+window_size])/window_size

        smas.append(sma)

    return smas
        