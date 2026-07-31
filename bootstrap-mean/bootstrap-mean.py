import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    # Write code here

    x = np.array(x, dtype=float)
    n = len(x)

    if rng is None:
        rng = np.random.defaul_rng()

    random_indices = rng.integers(0, n, size=(n_bootstrap, n))

    bootstrap_mean = np.mean(x[random_indices], axis=1)

    alpha = 1 - ci

    lower = np.quantile(bootstrap_mean, alpha/2)
    upper = np.quantile(bootstrap_mean, 1 - alpha/2)

    return bootstrap_mean, lower, upper
    pass
