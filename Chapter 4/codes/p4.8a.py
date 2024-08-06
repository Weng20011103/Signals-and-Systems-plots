import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return np.where((-0.5 <= x) & (x <= 0.5), x + 0.5, np.where(0.5 < x, 1, 0))

x = np.linspace(-2, 2, 10000)

# Create a figure with a specific size (width, height) in inches
plt.figure(figsize=(12, 2))

# Plot the function
plt.plot(x, f(x))

# Customize x-axis ticks and labels
x_ticks = [-0.5, 0.5]
x_labels = ['$-\dfrac{1}{2}$', '$\dfrac{1}{2}$']
plt.xticks(x_ticks, x_labels)

# Customize y-axis ticks and labels
y_ticks = [0, 1]
y_labels = ['0', '1']
plt.yticks(y_ticks, y_labels)

# Set a title for the plot
plt.title('x(t)')

# Add x = 0 and y = 0 axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.xlabel('t', loc='right')

# Display the plot
plt.show()