def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    # Write code here

    max_lag = max(lags)
    n = len(series)

    result = []

    for i in range(max_lag, n):
        row = [series[i - lag] for lag in lags]

        result.append(row)

    return result