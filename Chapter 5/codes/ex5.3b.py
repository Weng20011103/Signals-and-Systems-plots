import numpy as np
import matplotlib.pyplot as plt

def f(x):
  N_1 = 2
  y = np.sin(x*(N_1+0.5)) / np.sin(0.5*x)

  return y

x = np.linspace(-3*np.pi, 3*np.pi, 20000)

# Create a figure with a specific size (width, height) in inches
plt.figure(figsize=(12, 2))

# Plot the function
plt.plot(x, f(x))

# Customize x-axis ticks and labels
x_ticks = [-3*np.pi, -2*np.pi, -np.pi,0, np.pi, 2*np.pi, 3*np.pi]
x_labels = ['$-3\pi$', '$-2\pi$', '$-\pi$', '0', '$\pi$', '$2\pi$', '$\omega$']
plt.xticks(x_ticks, x_labels)

# Customize y-axis ticks and labels
y_ticks = [0, 5]
y_labels = ['0', '5']
plt.yticks(y_ticks, y_labels)

# Set a title for the plot
plt.title('$X(e^{j\omega})$')

# Add x = 0 and y = 0 axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.xlabel('t', loc='right')

# Display the plot
plt.show()