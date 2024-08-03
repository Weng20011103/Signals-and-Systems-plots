import numpy as np
import matplotlib.pyplot as plt

def x(t):
    T_1 = 1
    # Create an array of zeros with the same shape as t
    y = np.zeros_like(t)
    
    # Apply the piecewise conditions
    y[t < -T_1] = 0
    y[(-T_1 <= t) & (t < T_1)] = 1
    y[t > T_1] = 0

    return y

# Define the time range
t = np.linspace(-12, 12, 10000)

T=4

y = x(t+12)+x(t+8)+x(t+4)+x(t)+x(t-4)+x(t-8)+x(t-12)

# Plot the function
plt.plot(t, y)

# Customize x-axis ticks and labels
x_ticks = [-12, -8, -4, -2, -1, 1, 2, 4, 8, 12]
x_labels = ['-3T', '-2T', '-T', '-$\dfrac{T}{2}$', '-$T_1$', '$T_1$', '$\dfrac{T}{2}$', 'T', '2T', '3T']
plt.xticks(x_ticks, x_labels)

# Customize y-axis ticks and labels
y_ticks = [0, 1]
y_labels = ['0', '1']
plt.yticks(y_ticks, y_labels)

# Set the ylim
plt.ylim(-0.1, 2.1)

# Set a title for the plot
plt.title('x(t)')

# Add x = 0 and y = 0 axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.xlabel('t', loc='right')

# Display the plot
plt.show()
