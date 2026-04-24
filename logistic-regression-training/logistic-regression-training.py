import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    w = np.zeros(X.shape[1])
    b = 0.0

    for i in range(steps):
        z = np.dot(X, w) + b
        y_hat = _sigmoid(z)

        dz = y_hat - y
        dw = np.dot(X.T, dz)/X.shape[0]
        db = np.mean(dz)

        w = w - lr*dw
        b = b - lr*db

    return (w, b)
    pass