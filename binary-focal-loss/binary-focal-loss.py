import numpy as np

def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
    # Write code here

    predictions = np.array(predictions)
    targets = np.array(targets)

    p_t = np.where(targets == 1, predictions, 1 - predictions)

    focal_loss = - alpha * (1 - p_t)**gamma * np.log(p_t)

    return np.mean(focal_loss)