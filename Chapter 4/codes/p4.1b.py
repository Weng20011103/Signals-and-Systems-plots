import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = 4 / np.sqrt(4+x**2)

    return y

# Define the time range
x = np.linspace(-30, 30, 10000)

y = f(x)

# Plot the function
plt.plot(x, y)

# Customize x-axis ticks and labels
x_ticks = [0]
x_labels = ['0']
plt.xticks(x_ticks, x_labels)

# Customize y-axis ticks and labels
y_ticks = [0, 2]
y_labels = ['0', '2']
plt.yticks(y_ticks, y_labels)

# Set the ylim
plt.ylim(-0.1, 2.1)

# Set a title for the plot
plt.title('$|X(j\omega)|$')

# Add x = 0 and y = 0 axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.xlabel('$\omega$', loc='right')

# Display the plot
plt.show()
