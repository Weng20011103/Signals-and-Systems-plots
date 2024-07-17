import numpy as np
import matplotlib.pyplot as plt

# Define the discrete-time unit step function
def unit_step(n):
    return np.where(n >= 0, 1, 0)

# Generate a range of n values
n = np.arange(-5, 21, 1)

# Generate data for the subplots
y1 = unit_step(n) - unit_step(n-4)
y2 = unit_step(n-2) - unit_step(n-6)
y3 = unit_step(n-4) - unit_step(n-8)
y4 = unit_step(n-6) - unit_step(n-10)
y5 = unit_step(n-8) - unit_step(n-12)

# Create a figure with 5 vertical subplots
fig, axs = plt.subplots(5, 1, figsize=(8, 15))

# Plot data in each subplot
axs[0].stem(n, y1)
axs[1].stem(n, y2)
axs[2].stem(n, y3)
axs[3].stem(n, y4)
axs[4].stem(n, y5)

# x-ticks for subplots
for ax in axs:
    ax.set_xticks(n)

# Set different y-axis labels for each subplot
axs[0].set_ylabel('g[n]', rotation=0, labelpad=20)
axs[1].set_ylabel('g[n-2]', rotation=0, labelpad=20)
axs[2].set_ylabel('g[n-4]', rotation=0, labelpad=20)
axs[3].set_ylabel('g[n-6]', rotation=0, labelpad=20)
axs[4].set_ylabel('g[n-8]', rotation=0, labelpad=20)

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust rect to make space for the suptitle

plt.show()
