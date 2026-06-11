import numpy as np

def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    # Write code here

    predictions = np.array(predictions)

    q = np.zeros_like(predictions)
    K = len(q)

    for i in range(K):
        if i == target:
            q[i] = (1 - epsilon) + epsilon/K
        else:
            q[i] = epsilon/K

    loss = 0
    for i in range(K):
        loss -= q[i] * np.log(predictions[i])
        
    return loss