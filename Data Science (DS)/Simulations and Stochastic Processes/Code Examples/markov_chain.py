import numpy as np

states = ["Sunny", "Rainy"]
transition_matrix = np.array([[0.8, 0.2], [0.4, 0.6]])

def simulate_markov_chain(start_state=0, steps=10):
    state = start_state
    for _ in range(steps):
        print(states[state])
        state = np.random.choice([0, 1], p=transition_matrix[state])

simulate_markov_chain(1)

