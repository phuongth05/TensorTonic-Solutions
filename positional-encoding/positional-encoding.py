import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here

    positions = np.arange(seq_len)[:, np.newaxis]
    frequencies = np.arange(d_model)[np.newaxis, :]

    encoding = 1.0/(np.power(base, 2*(frequencies//2) /d_model))
    
    pe = positions * encoding

    pe[:, 0::2] = np.sin(pe[:, 0::2])
    pe[:, 1::2] = np.cos(pe[:, 1::2])

    return pe
    pass