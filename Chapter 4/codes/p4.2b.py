import numpy as np
import matplotlib.pyplot as plt

# Define the unit step function
def unit_step(t):
  return np.where(t >= 0, 1, 0)

# Define the continuous-time impulse function
def impulse(t):
  # Create an array of zeros with the same shape as t
  y = np.zeros_like(t)
    
  # Set the value to 1 when t is close to 0
  epsilon = 1e-3  # A small positive value
  y[np.abs(t) < epsilon] = 1

  return y

# Define the time range and the sine function
t = np.linspace(-5 , 5 , 20000)  # Time from -5 to 5 with 20000 points

# Generate data for the subplots
y1 = unit_step(-t-2) + unit_step(t-2)
y2 = -impulse(t+2) + impulse(t-2)

# Create a figure with 2 vertical subplots
fig, axs = plt.subplots(2, 1, figsize=(12, 8))

# Plot data in each subplot
axs[0].plot(t, y1)
axs[1].plot(t, y2)

# Customize x-axis ticks and labels
x_ticks = [-2, 2]
x_labels = ['-2', '2']

# Set x-ticks for subplots
for ax in axs:
  ax.set_xticks(x_ticks)

# Customize y-axis ticks and labels for each subplot
y_ticks_1 = [0, 1]
y_labels_1 = ['0', '1']
axs[0].set_yticks(y_ticks_1)
axs[0].set_yticklabels(y_labels_1)

y_ticks_2 = [-1, 0, 1]
y_labels_2 = ['-1', '0', '1']
axs[1].set_yticks(y_ticks_2)
axs[1].set_yticklabels(y_labels_2)

# Set y-axis limits for the first subplot
axs[0].set_ylim(-0.1, 2.1)

# Add x = 0 and y = 0 axes
for ax in axs:
  ax.axhline(0, color='black', linewidth=0.5)
  ax.axvline(0, color='black', linewidth=0.5)

# Set different title for each subplot
axs[0].set_title('u(-t-2)+u(t-2)')
axs[1].set_title('$-\delta(t+2)+\delta(t-2)$')

plt.show()