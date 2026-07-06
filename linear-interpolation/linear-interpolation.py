def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    # Write code here

    left = 0

    for i in range(len(values)):
        if (values[i] == None):
            right = [j for j in range(i, len(values)) if values[j] is not None][0]
            values[i] = values[left] + (i - left) / (right - left) * (values[right] - values[left])
        else: 
            left = i

    return values
                