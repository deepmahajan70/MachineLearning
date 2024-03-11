import numpy as np

# Define states as numbers for simplicity
states = {
    "Yellow": 0,
    "Red": 1,
    "Blue": 2
}

# Transition probability matrix
transition_matrix = np.array([
    [0.2, 0.6, 0.2],  # Yellow
    [0.3, 0.0, 0.7],  # Red
    [0.5, 0.0, 0.5]   # Blue
])

# Initial state probabilities based on observations
initial_probabilities = np.array([0.4, 0.2, 0.4])

# Number of days to simulate
num_days = 100000

# Combine initial probabilities and transition matrix
combined_matrix = np.vstack([initial_probabilities, transition_matrix])

# Loop for the number of days to reach stationary distribution
for _ in range(num_days - 1):
  # Update state probabilities using matrix multiplication
  combined_matrix = combined_matrix @ transition_matrix

# Stationary probabilities are the final row of the combined matrix
stationary_probabilities = combined_matrix[-1, :]

# Print results with state names for readability
for state, probability in zip(states.keys(), stationary_probabilities):
  print(f"Probability of wearing {state}: {probability:.4f}")
