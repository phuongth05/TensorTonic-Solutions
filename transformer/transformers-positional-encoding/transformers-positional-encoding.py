import numpy as np

def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    """
    Generate sinusoidal positional encodings.
    """
    # Your code here
    position = np.arange(seq_length).reshape(-1, 1)

    division = np.exp(np.arange(0, d_model, 2) * (-np.log(10000.0) / d_model))
    
    PE = np.zeros((seq_length, d_model), dtype=float)

    PE[:, 0::2] = np.sin(position * division)

    PE[:, 1::2] = np.cos(position * division)

    return PE
    pass