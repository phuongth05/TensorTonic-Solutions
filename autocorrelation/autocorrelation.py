import numpy as np

def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    # Write code here
    series = np.array(series)
    n = len(series)

    mean_n = 1/n * np.sum(series)

    var = np.sum((series - mean_n)**2)

    output = np.zeros(max_lag + 1)
    output[0] = 1.0

    if var == 0:
        for i in range(1, max_lag + 1):
            output[i] = 0.0

        return output.tolist()

    for i in range(1, max_lag + 1):
        output[i] = np.sum(
            [(series[j] - mean_n)*(series[j + i] - mean_n)/var 
             for j in range(n - i)]
        )

    return output.tolist()