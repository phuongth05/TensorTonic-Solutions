import numpy as np



def compute_advantage(states, rewards, V, gamma):
    """
    Returns: A (NumPy array of advantages)
    """
    # Write code here
    states = np.array(states)
    rewards = np.array(rewards)
    V = np.array(V)
    length = len(states)

    A = np.zeros_like(states, dtype=float)
    G = np.zeros_like(states, dtype=float)

    def compute_G(time):
        if time < length:
            G = gamma ** time * rewards[time]

        return G

    running_return = 0.0
    for t in reversed(range(length)):
        running_return = rewards[t] + gamma * running_return
        G[t] = running_return

    A = G - V

    return A
    pass
