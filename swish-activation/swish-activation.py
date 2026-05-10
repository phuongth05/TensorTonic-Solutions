import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here

    x = np.array(x)

    return x * 1.0/(1.0+np.exp(-x))
    pass