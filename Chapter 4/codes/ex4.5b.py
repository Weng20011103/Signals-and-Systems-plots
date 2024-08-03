import numpy as np
import matplotlib.pyplot as plt

def x(t):
    W = 1
    y = np.sin(t * W) / (np.pi * t)
    
    return y

# Define the time range
t = np.linspace(-20 , 20 , 10000)

y = x(t)

# Plot the function
plt.plot(t, y)

# Customize x-axis ticks and labels
x_ticks = [-6 * np.pi, -5 * np.pi, -4 * np.pi, -3 * np.pi, -2 * np.pi, -np.pi, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi, 5 * np.pi, 6 * np.pi]
x_labels = ['$-\dfrac{6π}{W}$', '$-\dfrac{5π}{W}$', '$-\dfrac{4π}{W}$', '$-\dfrac{3π}{W}$', '$-\dfrac{π}{W}$', '-$\dfrac{π}{W}$', '$\dfrac{π}{W}$', '$\dfrac{2π}{W}$', '$\dfrac{3π}{W}$', '$\dfrac{4π}{W}$', '$\dfrac{5π}{W}$', '$\dfrac{6π}{W}$']
plt.xticks(x_ticks, x_labels)

# Customize y-axis ticks and labels
y_ticks = [0, 1/np.pi]
y_labels = ['0', '$\dfrac{W}{π}$']
plt.yticks(y_ticks, y_labels)

# Set a title for the plot
plt.title('x(t)')

# Add x = 0 and y = 0 axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.xlabel('t', loc='right')

# Display the plot
plt.show()
