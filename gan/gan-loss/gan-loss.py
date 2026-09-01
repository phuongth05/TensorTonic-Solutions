import numpy as np

def discriminator_loss(real_probs, fake_probs):
    """Compute discriminator loss using binary cross-entropy.
    Returns: Loss value rounded to 4 decimals."""

    N = len(real_probs)
    
    real_probs = np.array(real_probs)
    fake_probs = np.array(fake_probs)

    real_probs = np.clip(real_probs, 1e-8, 1 - 1e-8)
    fake_probs = np.clip(fake_probs, 1e-8, 1 - 1e-8)

    return -1/N * np.sum(np.log(real_probs) + np.log(1 - fake_probs))
    pass

def generator_loss(fake_probs):
    """Compute non-saturating generator loss.
    Returns: Loss value rounded to 4 decimals."""

    N = len(fake_probs)

    fake_probs = np.array(fake_probs)

    fake_probs = np.clip(fake_probs, 1e-8, 1 - 1e-8)

    return -1/N * np.sum(np.log(fake_probs))
    pass