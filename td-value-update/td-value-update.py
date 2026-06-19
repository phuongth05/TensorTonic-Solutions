import numpy as np

def td_value_update(V, s, r, s_next, alpha, gamma):
    """
    Returns: updated value function V_new
    """
    # Write code here

    TD_Error = r + gamma * V[s_next] - V[s]

    V_new = V.copy()
    V_new[s] = V[s] + alpha * TD_Error

    return V_new
    pass