import numpy as np

def seasonal_average(series, period):
    """
    Compute the average value for each position in the seasonal cycle.
    """
    # Write code here
    n = len(series)

    series = np.array(series, dtype=float)

    output = []
    for p in range(period):
        output.append(np.mean(series[p::period]))

    return output