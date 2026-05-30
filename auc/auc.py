import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # Write code here
    if len(fpr) != len(tpr):
        return 0.0

    if len(fpr) < 2:
        return 0.0

    return np.trapezoid(tpr, fpr)
    pass