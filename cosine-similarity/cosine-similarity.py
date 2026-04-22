import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here

    a = np.array(a)
    b = np.array(b)

    len_1 = np.linalg.norm(a)
    len_2 = np.linalg.norm(b)

    if (len_1 == 0 or len_2 == 0):
        return 0.0

    return np.dot(a, b) / (len_1*len_2)
    pass