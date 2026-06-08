import numpy as np

def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here

    x1 = np.array(x1)
    x2 = np.array(x2)

    cos = (x1 @ x2) / (np.sqrt(x1@x1) * np.sqrt(x2@x2))

    if label == 1:
        return 1 - cos
    elif label == -1:
        return max(0, cos - margin)