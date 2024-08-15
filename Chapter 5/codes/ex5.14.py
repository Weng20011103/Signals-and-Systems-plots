import numpy as np
import matplotlib.pyplot as plt

# Define the unit step function
def unit_step(x):
    return np.where(x >= 0, 1, 0)

def f(x, ω):
  return unit_step(x+ω)-unit_step(x-ω)

x = np.linspace(-1.5*np.pi, 1.5*np.pi, 20000)

y = f(x+2*np.pi, np.pi/4) + f(x+np.pi, np.pi/4) + f(x, np.pi/4) + f(x-np.pi, np.pi/4) + f(x-2*np.pi, np.pi/4)

# Create a figure with a specific size (width, height) in inches
plt.figure(figsize=(12, 3))

# Plot the function
plt.plot(x, y)

# Customize x-axis ticks and labels
x_ticks = [-np.pi, -3*np.pi/4, -np.pi/4, np.pi/4, 3*np.pi/4, np.pi]
x_labels = ['$-\pi$', '$-\dfrac{3\pi}{4}$', '$-\dfrac{\pi}{4}$', '$\dfrac{\pi}{4}$', '$\dfrac{3\pi}{4}$', '$\pi$']
plt.xticks(x_ticks, x_labels)

# Customize y-axis ticks and labels
y_ticks = [0, 1]
y_labels = ['0', '1']
plt.yticks(y_ticks, y_labels)

# Set a title for the plot
plt.title('$H(e^{j\omega})$')

# Disable the frame
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_visible(False)

ax.spines['bottom'].set_position('zero')

# Add text to the right of the x-axis
ax.text(1.5*np.pi, -0.05, '$\omega$', ha='left', va='center')

# Add x = 0 and y = 0 axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Display the plot
plt.show()