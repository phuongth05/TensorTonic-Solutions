def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    # Write code here
    n = len(values) - window_size + 1
    result = []

    for i in range(n):
        value = sorted(values[i: i + window_size])

        if (len(value) % 2 == 0):
            result.append((value[len(value)//2 - 1] + value[len(value)//2]) / 2)
        else:
            result.append(value[len(value)//2])
            

    return result