import numpy as np
import matplotlib.pyplot as plt

# Define the discrete-time impulse function
def impulse(n):
    return np.where(n == 0, 1, 0)

def x(n):
    return impulse(n) + 2 * impulse(n-1) - impulse(n-3)

# Define the the response of the linear system to the shifted unit impulse
def h(n):
    return 2 * impulse(n+1) + 2 * impulse(n-1)

# Generate a range of n values
n = np.arange(-5, 6, 1)

# Generate data for the subplots
y1 = x(n)
y2 = h(-n)
y3 = h(-1) * x(n+1) + h(1) * x(n-1)

# Create a figure with 3 vertical subplots
fig, axs = plt.subplots(3, 1, figsize=(8, 15))

# Plot data in each subplot
axs[0].stem(n, y1)
axs[1].stem(n, y2)
axs[2].stem(n, y3)

# Set x-ticks only for the last subplot
axs[2].set_xticks(n)

# Hide x-ticks for other subplots
for ax in axs[:-1]:
    ax.set_xticks([])

# Label y-values for each point in axs
for i in range(len(n)):
    if y1[i] >= 0:
        axs[0].annotate(f'{y1[i]:.2f}', (n[i], y1[i]), textcoords="offset points", xytext=(0, 5), ha='center')
    else:
        axs[0].annotate(f'{y1[i]:.2f}', (n[i], y1[i]), textcoords="offset points", xytext=(0, -15), ha='center')

for i in range(len(n)):
    if y2[i] >= 0:
        axs[1].annotate(f'{y2[i]:.2f}', (n[i], y2[i]), textcoords="offset points", xytext=(0, 5), ha='center')
    else:
        axs[1].annotate(f'{y2[i]:.2f}', (n[i], y2[i]), textcoords="offset points", xytext=(0, -15), ha='center')

for i in range(len(n)):
    if y3[i] >= 0:
        axs[2].annotate(f'{y3[i]:.2f}', (n[i], y3[i]), textcoords="offset points", xytext=(0, 5), ha='center')
    else:
        axs[2].annotate(f'{y3[i]:.2f}', (n[i], y3[i]), textcoords="offset points", xytext=(0, -15), ha='center')

# Set different y-axis labels for each subplot
axs[0].set_ylabel('x[k]', rotation=0, labelpad=20)
axs[1].set_ylabel('h[-k]', rotation=0, labelpad=20)
axs[2].set_ylabel('y[n]', rotation=0, labelpad=20)

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust rect to make space for the suptitle

plt.show()
