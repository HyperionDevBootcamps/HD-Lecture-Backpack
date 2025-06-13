import numpy as np

# Simulate inter-arrival times (exponentially distributed)
lambda_requests = 5  # 5 requests per second
n_requests = 100
inter_arrival_times = np.random.exponential(1/lambda_requests, n_requests)

# Compute arrival times
arrival_times = np.cumsum(inter_arrival_times)
print("Arrival times:", arrival_times)

