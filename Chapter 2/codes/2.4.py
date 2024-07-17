import numpy as np
import matplotlib.pyplot as plt

# Define the discrete-time unit step function
def unit_step(n):
    return np.where(n >= 0, 1, 0)

def x(n):
    return unit_step(n-3) - unit_step(n-9)

def h(n):
    return unit_step(n-4) - unit_step(n-16)

# Generate a range of n values
n = np.arange(-20, 31, 1)

# Generate data for the subplots
y1 = x(n)
y2 = h(n)
y3 = h(-n)
y4 = h(n-3) + h(n-4) + h(n-5) + h(n-6) + h(n-7) + h(n-8)

# Create a figure with 4 vertical subplots
fig, axs = plt.subplots(4, 1, figsize=(8, 15))

# Plot data in each subplot
axs[0].stem(n, y1)
axs[1].stem(n, y2)
axs[2].stem(n, y3)
axs[3].stem(n, y4)

# x-ticks for subplots
for ax in axs:
    ax.set_xticks(n)

for i in range(len(n)):
    if y4[i] >= 0:
        axs[3].annotate(f'{y4[i]:.1f}', (n[i]+0.5, y4[i]-0.8), textcoords="offset points", xytext=(0, 5), ha='center')
    else:
        axs[3].annotate(f'{y4[i]:.1f}', (n[i]+0.5, y4[i]-0.8), textcoords="offset points", xytext=(0, -15), ha='center')

# Set different y-axis labels for each subplot
axs[0].set_ylabel('x[n]', rotation=0, labelpad=20)
axs[1].set_ylabel('h[n]', rotation=0, labelpad=20)
axs[2].set_ylabel('h[-k]', rotation=0, labelpad=20)
axs[3].set_ylabel('y[n]', rotation=0, labelpad=20)

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust rect to make space for the suptitle

plt.show()
