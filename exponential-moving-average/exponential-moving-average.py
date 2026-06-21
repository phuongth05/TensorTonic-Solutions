def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    # Write code here
    EMA = values.copy()
    n = len(EMA)

    for i in range(1, n):
        EMA[i] = alpha * values[i] + (1 - alpha) * EMA[i - 1]

    return EMA