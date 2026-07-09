import numpy as np

def rolling_std(values, window_size):
    """
    Compute the rolling population standard deviation.
    """
    # Write code here

    values = np.array(values)
    output = []

    for i in range(len(values) - window_size + 1):
        mean = np.mean([values[i + j] for j in range(window_size)])
        var = np.sqrt(1/window_size * np.sum([(values[i + j] - mean)**2 for j in range(window_size)]))

        output.append(var)

    return output