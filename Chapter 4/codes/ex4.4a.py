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
t = np.linspace(-6, 6, 10000)

y = x(t)

# Plot the function
plt.plot(t, y)

# Customize x-axis ticks and labels
x_ticks = [-1, 1]
x_labels = ['-T1', 'T1']
plt.xticks(x_ticks, x_labels)

# Customize y-axis ticks and labels
y_ticks = [0, 1]
y_labels = ['0', '1']
plt.yticks(y_ticks, y_labels)

# Set the ylim
plt.ylim(-0.2, 1.3)

# Set a title for the plot
plt.title('x(t)')

# Display the plot
plt.show()
