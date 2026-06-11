import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    # Write code here

    anchor = np.array(anchor)
    positive = np.array(positive)
    negative = np.array(negative)

    if anchor.ndim == 1:
        anchor = anchor.reshape(1, -1)
        positive = positive.reshape(1, -1)
        negative = negative.reshape(1, -1)

    d_ap = np.square(np.linalg.norm((anchor - positive), axis=1))
    d_an = np.square(np.linalg.norm((anchor - negative), axis=1))

    loss = np.maximum(0, d_ap - d_an + margin)

    return np.mean(loss)
    pass