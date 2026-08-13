import numpy as np

def compute_gradient_norm_decay(T: int, W_hh: np.ndarray) -> list:
    """
    Simulate gradient norm decay over T time steps.
    Returns list of gradient norms.
    """
    # YOUR CODE HERE

    spectral_norm = np.linalg.norm(W_hh, ord=2)

    gradient_norm = []
    gradient_norm.append(1.0)

    for i in range(1, T):
        gradient_norm.append(gradient_norm[i - 1] * spectral_norm)

    return gradient_norm
    pass