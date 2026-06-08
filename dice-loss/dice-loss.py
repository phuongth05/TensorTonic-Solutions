import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    # Write code here

    p = np.array(p).flatten()
    y = np.array(y).flatten()

    Dice_Coff = (2 * np.sum(p @ y) + eps)/(np.sum(p) + np.sum(y) + eps)

    return 1.0 - Dice_Coff
    pass