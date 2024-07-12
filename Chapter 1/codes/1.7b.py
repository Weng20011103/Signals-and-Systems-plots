import numpy as np
import matplotlib.pyplot as plt

# Define the time range and the sine function
t = np.linspace(-4 * np.pi, 4 * np.pi, 2000)  # Time from -4*pi to 4*pi with 2000 points

# Generate data for the subplots
y1 = np.sin(0.5*t)
y2 = np.sin(-0.5*t)
y3 = 0.5 * (y1 + y2)

# Create a figure with 3 vertical subplots
fig, axs = plt.subplots(3, 1, figsize=(8, 15))

# Plot data in each subplot
axs[0].plot(t, y1)
axs[1].plot(t, y2)
axs[2].plot(t, y3)

# Set a single title for the entire figure
fig.suptitle('y(t) = even part of sin(0.5t)', fontsize=16)

# Set x-ticks to multiples of pi/2
x_ticks = np.arange(-4 * np.pi, 4.5 * np.pi, 0.5 * np.pi)
x_labels = [f'{i/2}π' if i != 0 else '0' for i in range(-8, 9)]

# Set x-ticks only for the last subplot
axs[2].set_xticks(x_ticks, x_labels)

# Hide x-ticks for other subplots
for ax in axs[:-1]:
    ax.set_xticks([])

# Set common y-ticks for all subplots
for ax in axs:
    ax.set_yticks(np.arange(-1, 1.5, 0.5))

# Set different y-axis labels for each subplot
axs[0].set_ylabel('sin(0.5t)', rotation=0, labelpad=20)
axs[1].set_ylabel('sin(-0.5t)', rotation=0, labelpad=20)
axs[2].set_ylabel('y(t)', rotation=0, labelpad=20)

# Add x = 0 and y = 0 axes
for ax in axs:
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust rect to make space for the suptitle

plt.show()
