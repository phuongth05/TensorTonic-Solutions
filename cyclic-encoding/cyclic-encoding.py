import math

def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    # Write code here
    results = []
    for v in values: 
        theta = 2 * math.pi * v / period
        encoded = [math.sin(theta), math.cos(theta)]

        results.append(encoded)

    return results