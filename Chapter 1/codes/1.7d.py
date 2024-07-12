import numpy as np
import matplotlib.pyplot as plt

# Define the unit step function
def unit_step(t):
    return np.where(t >= 0, 1, 0)

# Define the time range and the sine function
t = np.linspace(-5 , 5 , 2000)  # Time from -5 to 5 with 2000 points

# Generate data for the subplots
y1 = np.e**(-5*t) * unit_step(t+2)
y2 = np.e**(5*t) * unit_step(-t+2)
y3 = 0.5 * (y1 + y2)

# Create a figure with 3 vertical subplots
fig, axs = plt.subplots(3, 1, figsize=(8, 15))

# Plot data in each subplot
axs[0].plot(t, y1)
axs[1].plot(t, y2)
axs[2].plot(t, y3)

# Set x-ticks to multiples of pi/2
x_ticks = np.arange(-5, 5, 0.5)

# Set x-ticks for subplots
for ax in axs:
    ax.set_xticks(x_ticks)

# Add x = 0 and y = 0 axes
for ax in axs:
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

# Set different title for each subplot
axs[0].set_title('(e)**(-5t) * u(t+2)')
axs[1].set_title('(e)**(5t) * u(-t+2)')
axs[2].set_title('even part of (e)**(-5t) * u(t+2)')

# Adjust layout to prevent overlap
plt.tight_layout(h_pad = 5)

plt.show()