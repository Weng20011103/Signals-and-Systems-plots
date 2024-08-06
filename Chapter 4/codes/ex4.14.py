import numpy as np
import matplotlib.pyplot as plt

def f(t):
  return np.where(t < -1, 0, 
                  np.where((-1 <= t) & (t < -0.5), np.sqrt(np.pi), 
                            np.where((-0.5 <= t) & (t < 0.5), 0.5 * np.sqrt(np.pi), 
                                    np.where((0.5 <= t) & (t < 1), np.sqrt(np.pi), 0))))
def q(t):
  return np.where(t < -1, 0, 
                  np.where((-1 <= t) & (t < 0), -np.sqrt(np.pi), 
                            np.where((0 <= t) & (t < 1), np.sqrt(np.pi), 0)))

# Define the time range and the sine function
t = np.linspace(-2 , 2 , 20000)  # Time from -5 to 5 with 20000 points

# Generate data for the subplots
y1 = f(t)
y2 = q(t)

# Create a figure with 2 vertical subplots
fig, axs = plt.subplots(2, 1, figsize=(12, 7))

# Plot data in each subplot
axs[0].plot(t, y1)
axs[1].plot(t, y2)

# Customize x-axis ticks and labels
x_ticks = [-1, -0.5, 0, 0.5, 1]
x_labels = ['-1', '-0.5', '0', '0.5', '1']

# Set x-ticks for subplots
for ax in axs:
  ax.set_xticks(x_ticks)
  ax.set_xticklabels(x_labels)

# Customize y-axis ticks and labels for each subplot
y_ticks_1 = [0, 0.5*np.sqrt(np.pi), np.sqrt(np.pi)]
y_labels_1 = ['0', '$\dfrac{\sqrt{\pi}}{2}$', '$\sqrt{\pi}$']
axs[0].set_yticks(y_ticks_1)
axs[0].set_yticklabels(y_labels_1)

y_ticks_2 = [-np.sqrt(np.pi), 0, np.sqrt(np.pi)]
y_labels_2 = ['$-j\sqrt{\pi}$', '0', '$j\sqrt{\pi}$']
axs[1].set_yticks(y_ticks_2)
axs[1].set_yticklabels(y_labels_2)

# Add x = 0 and y = 0 axes
for ax in axs:
  ax.axhline(0, color='black', linewidth=0.5)
  ax.axvline(0, color='black', linewidth=0.5)

# Set different title for each subplot
axs[0].set_title('$X(j\omega)$')
axs[1].set_title('$X(j\omega)$')

axs[0].set_xlabel('$\omega$', loc='right')
axs[1].set_xlabel('$\omega$', loc='right')

plt.show()