def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here
    differences = series
    
    for ord in range(order):
        size = len(differences)
        differences = [differences[i] - differences[i - 1] for i in range(1, size)]

    return differences