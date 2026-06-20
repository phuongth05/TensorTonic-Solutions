def sarsa_update(q_table, state, action, reward, next_state, next_action, alpha, gamma):
    """
    Perform one SARSA update and return the updated Q-table.
    """
    # Write code here

    error = (reward
    + gamma 
    * q_table[next_state][next_action] 
    - q_table[state][action])

    q_new = q_table.copy()

    q_new[state][action] += alpha * error

    return q_new