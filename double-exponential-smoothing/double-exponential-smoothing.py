def double_exponential_smoothing(series, alpha, beta):
    """
    Apply Holt's linear trend method and return the level values.
    """
    # Write code here

    levels = []
    n = len(series)

    level_i_1 = series[0]
    levels.append(level_i_1)
    
    trend_i_1 = series[1] - series[0]

    for i in range(1, n):
        level_i = alpha * series[i] + (1 - alpha) * (level_i_1 + trend_i_1)

        trend_i = beta * (level_i - level_i_1) + (1 - beta) * trend_i_1

        levels.append(level_i)
        level_i_1 = level_i
        trend_i_1 = trend_i

    return levels