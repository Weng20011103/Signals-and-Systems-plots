import numpy as np
import matplotlib.pyplot as plt

# Define the unit step function
def unit_step(t):
  return np.where(t >= 0, 1, 0)

def f(t):
  y = -1.5 * t + np.pi

  y = np.where(y > 3 * np.pi, y - 4 * np.pi, y)
  y = np.where(y > np.pi, y - 2 * np.pi, y)
  y = np.where(y < -np.pi, y + 2 * np.pi, y)

  return y

# Define the time range and the sine function
t = np.linspace(-5 , 5 , 20000)  # Time from -5 to 5 with 20000 points

# Generate data for the subplots
y1 = 2 * (unit_step(t+3) - unit_step(t-3))
y2 = f(t)

# Create a figure with 2 vertical subplots
fig, axs = plt.subplots(2, 1, figsize=(12, 8))

# Plot data in each subplot
axs[0].plot(t, y1)
axs[1].plot(t, y2)

# Customize x-axis ticks and labels
x_ticks = [-3, -2*np.pi/3, 2*np.pi/3, 3]
x_labels = ['-3', '$-\dfrac{2\pi}{3}$', '$\dfrac{2\pi}{3}$', '3']

# Set x-ticks for subplots
for ax in axs:
  ax.set_xticks(x_ticks)
  ax.set_xticklabels(x_labels)

# Customize y-axis ticks and labels for each subplot
y_ticks_1 = [0, 2]
y_labels_1 = ['0', '2']
axs[0].set_yticks(y_ticks_1)
axs[0].set_yticklabels(y_labels_1)

y_ticks_2 = [-np.pi, 0, np.pi]
y_labels_2 = ['$-\pi$', '0', '$\pi$']
axs[1].set_yticks(y_ticks_2)
axs[1].set_yticklabels(y_labels_2)

# Set y-axis limits for the first subplot
axs[0].set_ylim(-0.1, 3.1)

# Add x = 0 and y = 0 axes
for ax in axs:
  ax.axhline(0, color='black', linewidth=0.5)
  ax.axvline(0, color='black', linewidth=0.5)

# Add the horizontal lines
axs[1].axhline(y=np.pi, xmin=0, xmax=1, color='red', linestyle='--')
axs[1].axhline(y=-np.pi, xmin=0, xmax=1, color='red', linestyle='--')

# Set different title for each subplot
axs[0].set_title('$|X(j\omega)|$')
axs[1].set_title('$\sphericalangle X(j\omega)$')

plt.show()