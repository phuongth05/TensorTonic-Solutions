def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    # Write code here
    pct = []

    for i in range(1, len(series)):
        if series[i - 1] != 0:
            pct.append((series[i] - series[i - 1]) / series[i - 1])
        else:
            pct.append(0.0)
    return pct