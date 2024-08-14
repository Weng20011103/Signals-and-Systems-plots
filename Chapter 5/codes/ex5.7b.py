import numpy as np
import matplotlib.pyplot as plt

# Define the unit step function
def unit_step(x):
    return np.where(x >= 0, 1, 0)

def f(x, ω):
  return unit_step(x+ω)-unit_step(x-ω)

x = np.linspace(-3*np.pi, 3*np.pi, 20000)

# Create a figure with a specific size (width, height) in inches
plt.figure(figsize=(12, 2))

# Plot the function
plt.plot(x, f(x+4*np.pi-np.pi, 1)+f(x+2*np.pi-np.pi, 1)+f(x-np.pi, 1)+f(x-2*np.pi-np.pi, 1))

# Customize x-axis ticks and labels
x_ticks = [-3*np.pi, -2*np.pi, -np.pi, -np.pi+1, 0, np.pi-1, np.pi, 2*np.pi, 3*np.pi]
x_labels = ['$-3\pi$', '$-2\pi$', '$-\pi$', '$-(\pi-\omega_c)$', '0', '$(\pi-\omega_c)$','$\pi$', '$2\pi$', '$\omega$']
plt.xticks(x_ticks, x_labels)

# Customize y-axis ticks and labels
y_ticks = [0, 1]
y_labels = ['0', '1']
plt.yticks(y_ticks, y_labels)

# Set a title for the plot
plt.title('$H_{lp}(e^{j(\omega-\pi)})$')

# Add x = 0 and y = 0 axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.xlabel('t', loc='right')

# Display the plot
plt.show()