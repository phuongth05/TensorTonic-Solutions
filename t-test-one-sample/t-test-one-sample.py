import numpy as np
import math

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here

    x = np.array(x)
    x_mean = np.mean(x)

    s = math.sqrt(1/(len(x) - 1) * np.sum((x - x_mean)**2))

    t = (x_mean - mu0)/(s/math.sqrt(len(x)))

    return t
    pass