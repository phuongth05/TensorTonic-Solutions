import numpy as np

def rnn_forward(X: np.ndarray, h_0: np.ndarray,
                W_xh: np.ndarray, W_hh: np.ndarray, b_h: np.ndarray) -> tuple:
    """
    Forward pass through entire sequence.
    """
    # YOUR CODE HERE

    T = X.shape[-2]

    h = h_0
    h_list = []

    for t in range(T):
        x = X[:, t, :]
        h = np.tanh(x @ W_xh.T + h @ W_hh.T + b_h)

        h_list.append(h)
        
    return (np.stack(np.array(h_list), axis=1), h)
    pass