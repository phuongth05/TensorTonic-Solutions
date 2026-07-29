import numpy as np

def discount_returns(rewards, gamma):
    """
    Compute the discounted return at every timestep.
    """
    # Write code here

    rewards = np.array(rewards, dtype=float)

    G = np.zeros_like(rewards)

    T = len(G)

    G[T - 1] = rewards[T - 1]

    t = T - 2
    while t >= 0:
        G[t] = rewards[t] + gamma * G[t + 1]
        t -= 1

    return G
    