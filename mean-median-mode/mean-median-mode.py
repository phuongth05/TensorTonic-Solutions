import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.array(x, dtype=float)
    
    mean = np.mean(x)
    median = np.median(x)

    x_cnt = Counter(x)
    max_cnt = max(x_cnt.values())
    modes = []

    for value, cnt in x_cnt.items():
        if cnt == max_cnt:
            modes.append(value)

    mode = min(modes)
    return mean, median, mode
    pass