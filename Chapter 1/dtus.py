import numpy as np
import matplotlib.pyplot as plt

# Define the discrete-time unit step function
def unit_step(n):
    return np.where(n >= 0, 1, 0)

# Generate a range of n values
n = np.arange(-10, 11, 1)

# Compute the unit step values
u = unit_step(n)

# Create a figure with a larger horizontal size
plt.figure(figsize=(12, 4))

# Plot the unit step function
plt.stem(n, u)
plt.title('Discrete-Time Unit Step Function')
plt.xlabel('n')
plt.ylabel('u[n]', rotation=0)  # Make y-axis label horizontal
plt.grid(False)

# Set x-axis labels to use the values from n
plt.xticks(n)

y_ticks= np.arange(0, 2, 1)

# Set y-axis labels to use the values from y_ticks
plt.yticks(y_ticks)

plt.show()
