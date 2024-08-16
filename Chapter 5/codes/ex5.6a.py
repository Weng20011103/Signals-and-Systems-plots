import numpy as np
import matplotlib.pyplot as plt

def x(n):
    return np.where(n == 0, 1, 0)

N = 10

# Generate a range of n values
n = np.arange(-25, 26, 1)

y = x(n+2*N) + x(n+N) + x(n) + x(n-N) + x(n-2*N)

# Create a figure with a specific size (width, height) in inches
plt.figure(figsize=(12, 2))

# Plot the unit step function
plt.stem(n, y)
plt.title('x[n]')
plt.grid(False)

xticks= [0]
xlabels = [str(i) for i in xticks]
xticks = np.append(xticks, N)
xlabels = np.append(xlabels, 'N')
xticks = np.append(xticks, 2*N)
xlabels = np.append(xlabels, '2N')
xticks = np.append(xticks, -N)
xlabels = np.append(xlabels, '-N')
xticks = np.append(xticks, -2*N)
xlabels = np.append(xlabels, '-2N')
# Set x-axis labels to use the values from n
plt.xticks(xticks, labels=xlabels)

yticks= [0, 1]
# Set y-axis labels to use the values from y_ticks
plt.yticks(yticks, labels=[str(i) for i in yticks])

# Disable the frame
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_visible(False)

ax.spines['bottom'].set_position('zero')

# Add text to the right of the x-axis
ax.text(26, 0, 'n', ha='left', va='center')

plt.show()
