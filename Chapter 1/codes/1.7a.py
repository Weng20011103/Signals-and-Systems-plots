import numpy as np
import matplotlib.pyplot as plt

# Define the discrete-time unit step function
def unit_step(n):
    return np.where(n >= 0, 1, 0)

# Generate a range of n values
n = np.arange(-10, 11, 1)

# Generate data for the subplots
y1 = unit_step(n)
y2 = unit_step(n-4)
y3 = unit_step(-n)
y4 = unit_step(-n-4)
y5 = 0.5 * (y1 - y2 + y3 - y4)

# Create a figure with 5 vertical subplots
fig, axs = plt.subplots(5, 1, figsize=(8, 15))

# Plot data in each subplot
axs[0].stem(n, y1)
axs[1].stem(n, y2)
axs[2].stem(n, y3)
axs[3].stem(n, y4)
axs[4].stem(n, y5)

# Set a single title for the entire figure
fig.suptitle('y[n] = even part of u[n] - u[n-4]', fontsize=16)

# Set x-ticks only for the last subplot
axs[4].set_xticks(n)

# Hide x-ticks for other subplots
for ax in axs[:-1]:
    ax.set_xticks([])

# Set common y-ticks for all subplots
for ax in axs:
    ax.set_yticks(np.arange(-2, 3, 1))

# Label y-values for each point in axs[4]
for i in range(len(n)):
    if y5[i] >= 0:
        axs[4].annotate(f'{y5[i]:.2f}', (n[i], y5[i]), textcoords="offset points", xytext=(0, 5), ha='center')
    else:
        axs[4].annotate(f'{y5[i]:.2f}', (n[i], y5[i]), textcoords="offset points", xytext=(0, -15), ha='center')

# Set different y-axis labels for each subplot
axs[0].set_ylabel('u[n]', rotation=0, labelpad=20)
axs[1].set_ylabel('u[n-4]', rotation=0, labelpad=20)
axs[2].set_ylabel('u[-n]', rotation=0, labelpad=20)
axs[3].set_ylabel('u[-n-4]', rotation=0, labelpad=20)
axs[4].set_ylabel('y[n]', rotation=0, labelpad=20)

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust rect to make space for the suptitle

plt.show()
