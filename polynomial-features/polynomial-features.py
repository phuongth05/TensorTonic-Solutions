def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here

    results = []
    for value in values:
        result = [value**p for p in range(degree + 1)]

        results.append(result)

    return results