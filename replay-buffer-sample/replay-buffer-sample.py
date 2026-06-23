import numpy as np

def replay_buffer_sample(buffer, batch_size, seed):
    """
    Sample a batch of transitions from the replay buffer.
    """
    # Write code here

    rng = np.random.RandomState(seed=seed)

    batch_number = rng.choice(len(buffer), size=batch_size, replace=False)

    return [buffer[int(i)] for i in batch_number]