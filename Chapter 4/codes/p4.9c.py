import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return np.where((-1 <= x) & (x <= 1), 0.5 * x + 0.5, 0)

x = np.linspace(-2, 2, 10000)

# Create a figure with a specific size (width, height) in inches
plt.figure(figsize=(12, 2))

# Plot the function
plt.plot(x, 0.5 * (f(x)+f(-x)))

# Customize x-axis ticks and labels
x_ticks = [-1, 1]
x_labels = ['-1', '1']
plt.xticks(x_ticks, x_labels)

# Customize y-axis ticks and labels
y_ticks = [0, 0.5, 1]
y_labels = ['0', '$\dfrac{1}{2}$','1']
plt.yticks(y_ticks, y_labels)

# Set a title for the plot
plt.title('The even part of x(t)')

# Add x = 0 and y = 0 axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.xlabel('t', loc='right')

# Display the plot
plt.show()