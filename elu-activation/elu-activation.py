import numpy as np
import math

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here    
    x = [val if val > 0 else alpha*(math.exp(val) - 1) for val in x]

    return x