import numpy as np
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here

    values = np.array(values)

    if num_bins == 0:
        return [0] * len(values)

    max_val = max(values)
    min_val = min(values)

    if max_val == min_val:
        return [0] * len(values)

    w = (max_val - min_val)/num_bins

    bins = []
    for v in values:
        bin = int((v - min_val)/w)

        if bin == num_bins:
            bin -= 1

        bins.append(bin)

    
    return bins