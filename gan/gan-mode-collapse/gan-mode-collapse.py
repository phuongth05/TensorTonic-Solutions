import numpy as np

def detect_mode_collapse(generated_samples, threshold=0.1):
    """
    Returns: dict with "diversity_score" (float) and "is_collapsed" (bool)
    """
    # Your implementation here

    std_devs = np.std(generated_samples, axis=0)

    mean_std = np.mean(std_devs)

    return {
        'diversity_score': mean_std,
        'is_collapsed': mean_std < threshold
    }
    pass