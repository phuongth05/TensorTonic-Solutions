import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y = np.array(y)
    _, counts = np.unique(y, return_counts=True)

    p = counts/counts.sum()

    p = p[p > 0]

    entropy = -np.sum(p * np.log2(p))

    return entropy
    pass