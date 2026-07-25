import numpy as np

def q_learning_update(Q, s, a, r, s_next, alpha, gamma):
    """
    Returns: updated Q-table Q_new
    """
    # Write code here
    
    Q_new = np.array(Q, dtype=float)

    max_next_q = np.max(Q_new[s_next])
    target = r + gamma * max_next_q

    Qsa_old = Q_new[s, a]

    Q_new[s, a] = Q_new[s, a] + alpha * (target - Q_new[s, a])
    
    return Q_new
    pass