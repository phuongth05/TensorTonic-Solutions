def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    # Write code here

    cum = []
    cum.append(0.0)

    for i in range(len(returns)):
        cum.append((1+ cum[i]) * (1 + returns[i]) - 1)

    cum.pop(0)
    return cum