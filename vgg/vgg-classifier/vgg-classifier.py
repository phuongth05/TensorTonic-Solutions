import numpy as np

def vgg_classifier(features: np.ndarray, W1: np.ndarray, b1: np.ndarray,
                   W2: np.ndarray, b2: np.ndarray, W3: np.ndarray, b3: np.ndarray) -> np.ndarray:
    """
    Returns: np.ndarray of shape (B, num_classes) with classification logits
    """
    # Your implementation here

    x = features.reshape(features.shape[0], -1)
    
    x = np.maximum(x @ W1 + b1, 0)

    x = np.maximum(x @ W2 + b2, 0)

    return x @ W3 + b3
    pass