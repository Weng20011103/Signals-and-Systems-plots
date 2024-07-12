import numpy as np
import matplotlib.pyplot as plt

# Define the discrete-time unit step function
def unit_step(n):
    return np.where(n >= 0, 1, 0)

# Generate a range of n values
n = np.arange(-10, 11, 1)

# Generate data for the subplots
y1 = (0.5)**n * unit_step(n-3)
y2 = (0.5)**(-n) * unit_step(-n-3)
y3 = y1 + y2

# Create a figure with 3 vertical subplots
fig, axs = plt.subplots(3, 1, figsize=(8, 15))

# Plot data in each subplot
axs[0].stem(n, y1)
axs[1].stem(n, y2)
axs[2].stem(n, y3)

# Set x-ticks for subplots
for ax in axs:
    ax.set_xticks(n)

# Set different title for each subplot
axs[0].set_title('(0.5)**n * u[n-3]')
axs[1].set_title('(0.5)**(-n) * u[-n-3]')
axs[2].set_title('even part of (0.5)**n * u[n-3]')

# Adjust layout to prevent overlap
plt.tight_layout(h_pad = 5)

plt.show()