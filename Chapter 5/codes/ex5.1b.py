import numpy as np
import matplotlib.pyplot as plt

def magnitude(t):
  a = -0.5
  y = 1 / np.sqrt(np.square(1-a*np.cos(t))+np.square(a*np.sin(t)))

  return y

def f(t):
  a = -0.5
  y = -np.arctan(a*np.sin(t)/(1-a*np.cos(t)))
  
  return y

# Define the time range and the sine function
t = np.linspace(-3 * np.pi , 3 * np.pi , 20000)  # Time from -5 to 5 with 20000 points

# Generate data for the subplots
y1 = magnitude(t)
y2 = f(t)

# Create a figure with 2 vertical subplots
fig, axs = plt.subplots(2, 1, figsize=(12, 8))

# Plot data in each subplot
axs[0].plot(t, y1)
axs[1].plot(t, y2)

# Customize x-axis ticks and labels
x_ticks = [-3*np.pi, -2*np.pi, -np.pi, 0, np.pi, 2*np.pi, 3*np.pi]
x_labels = ['$-3\pi$', '$-2\pi$', '$-\pi$', '0', '$\pi$', '$2\pi$', '$3\pi$']

# Set x-ticks for subplots
for ax in axs:
  ax.set_xticks(x_ticks)
  ax.set_xticklabels(x_labels)

# Customize y-axis ticks and labels for each subplot
y_ticks_1 = [0, 2/3, 2]
y_labels_1 = ['0', '$\dfrac{1}{1-a}$', '$\dfrac{1}{1+a}$']
axs[0].set_yticks(y_ticks_1)
axs[0].set_yticklabels(y_labels_1)

y_ticks_2 = [-np.arctan(0.5/np.sqrt(1-0.5**2)), 0, np.arctan(0.5/np.sqrt(1-0.5**2))]
y_labels_2 = [r'$-\tan^{-1}(|a|/\sqrt{1-a^2})$', '0', r'$\tan^{-1}(|a|/\sqrt{1-a^2})$']
axs[1].set_yticks(y_ticks_2)
axs[1].set_yticklabels(y_labels_2)

# Add x = 0 and y = 0 axes
for ax in axs:
  ax.axhline(0, color='black', linewidth=0.5)
  ax.axvline(0, color='black', linewidth=0.5)

# Set different title for each subplot
axs[0].set_title('$|X(e^{j\omega})|$')
axs[1].set_title('$\sphericalangle X(e^{j\omega})$')

plt.show()