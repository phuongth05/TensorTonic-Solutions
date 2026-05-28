import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here

    x = np.array(x)
    gamma = np.array(gamma)
    beta = np.array(beta)
    
    
    if x.ndim == 2:
        m = x.shape[0]
        _mean = 1/m * np.sum(x, axis=0, keepdims=True)
        _var = 1/m * np.sum((x - _mean)**2, axis=0, keepdims=True)
    
    elif x.ndim == 4:
        m = x.shape[0] * x.shape[2] * x.shape[3]
        _mean = 1/m * np.sum(x, axis=(0, 2, 3), keepdims=True)
        _var = 1/m * np.sum((x - _mean)**2, axis=(0, 2, 3), keepdims=True)
        beta = beta.reshape(1, -1, 1, 1)
        gamma = gamma.reshape(1, -1, 1, 1)
        
    x_hat = (x - _mean) / np.sqrt(_var + eps)
    y_hat = gamma * x_hat + beta

    return y_hat
    pass