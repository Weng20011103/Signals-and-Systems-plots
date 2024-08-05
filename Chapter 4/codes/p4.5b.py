import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return -2 * np.sin(3*t-4.5) / (np.pi*(t-1.5))

# Define the time range
t = np.linspace(-12, 12, 10000)

# Create a figure with a specific size (width, height) in inches
plt.figure(figsize=(12, 4))

# Plot the function
plt.plot(t, x(t))

# Customize x-axis ticks and labels
x_ticks = [-12, -4*np.pi/3+1.5, -2*np.pi/3+1.5, 1.5, 2*np.pi/3+1.5, 12]
x_labels = ['-12', '$-\dfrac{4\pi}{3}+\dfrac{3}{2}$', '$-\dfrac{2\pi}{3}+\dfrac{3}{2}$', '-$\dfrac{3}{2}$', '$\dfrac{2\pi}{3}+\dfrac{3}{2}$', '12']
plt.xticks(x_ticks, x_labels)

# Customize y-axis ticks and labels
y_ticks = [-6/np.pi, -1.5, -1, -0.5, 0, 0.5]
y_labels = ['$-\dfrac{6}{\pi}$', '-1.5', '-1', '-0.5', '0', '0.5']
plt.yticks(y_ticks, y_labels)

# Set a title for the plot
plt.title('x(t)')

# Add x = 0 and y = 0 axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.axhline(y=-6/np.pi, xmin=0, xmax=0.55, color='red', linestyle='--')

plt.xlabel('t', loc='right')

# Display the plot
plt.show()