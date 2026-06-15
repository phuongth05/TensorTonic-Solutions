import numpy as np

def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    # Write code here

    values = np.array(values)
    values_sorted = np.sort(values)

    n = len(values)

    if n < 2:
        return np.zeros_like(values)

    def get_median(arr):
        m = len(arr)

        if m%2 != 0:
            return arr[m//2]
        
        return (arr[m//2 - 1] + arr[m//2])/2

    if n%2 != 0:
        lower = values_sorted[:n//2]
        upper = values_sorted[n//2 + 1:]
    else:
        lower = values_sorted[:n//2]
        upper = values_sorted[n//2:]

    median = get_median(values_sorted)
    Q1 = get_median(lower)
    Q3 = get_median(upper)

    return (values - median)/(Q3 - Q1) if Q1 != Q3 else np.zeros_like(values)