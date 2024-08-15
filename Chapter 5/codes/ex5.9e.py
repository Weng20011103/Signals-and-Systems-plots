import numpy as np
import matplotlib.pyplot as plt

def x(n):
    return np.where(n >= -2, np.where(n <= 2, 1, 0), 0)

# Generate a range of n values
n = np.arange(-5, 6, 1)

# Compute the unit step values
u = x(n)

# Create a figure with a specific size (width, height) in inches
plt.figure(figsize=(12, 3))

# Plot the unit step function
plt.stem(n, u)
plt.title('x[n]')
plt.grid(False)

xticks= [0]
xlabels = [str(i) for i in xticks]
xticks = np.append(xticks, -2)
xlabels = np.append(xlabels, '$-N_1$')
xticks = np.append(xticks, 2)
xlabels = np.append(xlabels, '$N_1$')
xticks = np.append(xticks, 5)
xlabels = np.append(xlabels, 'n')
# Set x-axis labels to use the values from n
plt.xticks(xticks, labels=xlabels)

yticks= [0, 1]
# Set y-axis labels to use the values from y_ticks
plt.yticks(yticks, labels=[str(i) for i in yticks])

# Disable the frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.show()
