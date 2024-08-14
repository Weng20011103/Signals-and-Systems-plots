import numpy as np
import matplotlib.pyplot as plt

def x(n):
    a = 0.6
    return np.where(n >= 0, a**n, a**(-n))

# Generate a range of n values
n = np.arange(-10, 11, 1)

# Compute the unit step values
u = x(n)

# Create a figure with a specific size (width, height) in inches
plt.figure(figsize=(12, 2))

# Plot the unit step function
plt.stem(n, u)
plt.title('x[n]')
plt.grid(False)

xticks= np.arange(-5, 6, 1)
xlabels = [str(i) for i in xticks]
xticks = np.append(xticks, 10)
xlabels = np.append(xlabels, 'n')
# Set x-axis labels to use the values from n
plt.xticks(xticks, labels=xlabels)

y_ticks= []
# Set y-axis labels to use the values from y_ticks
plt.yticks(y_ticks)

plt.show()
