import numpy as np

def monte_carlo_pi(n_samples=10000):
    x = np.random.rand(n_samples)
    y = np.random.rand(n_samples)
    inside_circle = (x**2 + y**2) <= 1
    return (inside_circle.sum() / n_samples) * 4

print("Estimated π:", monte_carlo_pi(1000000000))

