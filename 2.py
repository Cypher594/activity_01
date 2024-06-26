import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

random_values = [-3.5, -1.2, 0, 2.8, -4.1, 1.5, -0.7, 3.2, -2.4, 4.6]

for val in random_values:
    print(f"Sigmoid of {val}: {sigmoid(val)}")

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

random_values = [-3.5, -1.2, 0, 2.8, -4.1, 1.5, -0.7, 3.2, -2.4, 4.6]

for val in random_values:
    print(f"Sigmoid of {val}: {sigmoid(val)}")


def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

def tanh(x):
    return np.tanh(x)

print("ReLU Output:")
for val in random_values:
    print(f"ReLU of {val}: {relu(val)}")

print("\nLeaky ReLU Output:")
for val in random_values:
    print(f"Leaky ReLU of {val}: {leaky_relu(val)}")

print("\nTanh Output:")
for val in random_values:
    print(f"Tanh of {val}: {tanh(val)}")
