import numpy as np

def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    n = len(y_true)

    bin_idx = np.floor(y_pred * n_bins).astype(int)
    bin_idx = np.clip(bin_idx, 0, n_bins - 1)

    ECE = 0.0

    for m in range(n_bins):
        in_bin = (bin_idx == m)
        bin_size = np.sum(in_bin)

        if bin_size == 0:
            continue

        bin_acc = np.mean(y_true[in_bin])
        bin_conf = np.mean(y_pred[in_bin])
        
        ECE += (bin_size / n) * np.abs(bin_acc - bin_conf)
        
    return float(ECE)
    
    pass