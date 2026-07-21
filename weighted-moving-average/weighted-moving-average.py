def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    # Write code here
    output = []
    w_sum = sum(weights)
    k = len(weights)
    
    for i in range(len(values)- k + 1):
        weighted_sum = sum(weights[j] * values[i + j] for j in range(k))/w_sum

        output.append(weighted_sum)
    
    return output