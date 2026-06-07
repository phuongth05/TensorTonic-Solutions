import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    # Write code here
    g = np.array(g)
    g_norm = np.sqrt(np.sum(np.square(g)))

    if g_norm == 0:
        return g

    if max_norm <= 0:
        return g

    g_clipped = []
    if g_norm > max_norm:
        g_clipped = [gr * max_norm / g_norm for gr in g]
    else:
        g_clipped = g

    return np.array(g_clipped)
    pass