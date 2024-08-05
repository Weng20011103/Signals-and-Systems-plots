import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return 2 * np.abs(np.cos(x))

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

for i in range(-6, 7, 1):
  x_ticks.append(i * np.pi * 0.5)
  x_labels.append(r'$\dfrac{' + str(i) + r'\pi}{2}$')

# Change the middle term
x_labels[5] = '0'

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