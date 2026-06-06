import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here

    y_pred =  [max(eps, min(pred, 1 - eps)) for pred in y_pred]

    Loss = [(-(true * math.log(pred) + (1 - true) * math.log(1 - pred))) for pred, true in zip(y_pred, y_true)]

    return Loss
    pass