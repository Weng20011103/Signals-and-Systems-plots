import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return 2 * np.abs(np.sin(2*x))

# Define the time range
x = np.linspace(-10, 10, 10000)

y = f(x)

# Create a figure with a specific size (width, height) in inches
plt.figure(figsize=(12, 4))

# Plot the function
plt.plot(x, y)

# Customize x-axis ticks and labels
x_ticks = []
x_labels = []

for i in range(-3, 4, 1):
  x_ticks.append(i * np.pi)
  x_labels.append(str(i) + r'$\pi$')

# Change the middle term
x_labels[3] = '0'

x_labels[2] = '$-\pi$'
x_labels[4] = '$\pi$'

plt.xticks(x_ticks, x_labels)

# Customize y-axis ticks and labels
y_ticks = [0, 2]
y_labels = ['0', '2']
plt.yticks(y_ticks, y_labels)

# Set the ylim
plt.ylim(-0.1, 3.1)

# Set a title for the plot
plt.title('$|X(j\omega)|$')

# Add x = 0 and y = 0 axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.xlabel('$\omega$', loc='right')

# Display the plot
plt.show()