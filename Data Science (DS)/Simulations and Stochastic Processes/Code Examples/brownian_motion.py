import numpy as np
import matplotlib.pyplot as plt

T = 1.0  
N = 10000  
dt = T/N
mu, sigma = 0.1, 0.2
S0 = 100
W = np.random.randn(N) * np.sqrt(dt)
S = S0 * np.exp(np.cumsum((mu - 0.5 * sigma**2) * dt + sigma * W))

plt.plot(S)
plt.title("Stock Price Simulation (Brownian Motion)")
plt.show()

