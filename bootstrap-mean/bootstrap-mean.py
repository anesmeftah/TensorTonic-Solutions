import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    # Write code here
    gen = np.random.default_rng(seed)
    n = len(x)
    x = np.asarray(x)
    
    means = np.empty(n_bootstrap)
    for i in range(n_bootstrap):
        indices = gen.integers(0, n, size=n)
        x_r = x[indices]
        means[i] = np.mean(x_r)
    bootstrap_means = np.mean(means)

    alpha = 1 - ci
    lower = np.percentile(means , 100 * alpha /2)
    upper = np.percentile(means , 100 * (1 - alpha/2))

    Output = {"bootstrap_mean": bootstrap_means, "lower": lower, "upper": upper}
    return Output

