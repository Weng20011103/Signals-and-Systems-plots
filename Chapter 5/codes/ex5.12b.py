import numpy as np
import matplotlib.pyplot as plt

def h(n, ω):
    return np.where(n == 0, ω / np.pi, np.sin(ω*n) / (np.pi*n))

# Generate a range of n values
n = np.arange(-10, 11, 1)

y = h(n, 1)

# Create a figure with a specific size (width, height) in inches
plt.figure(figsize=(12, 3))

# Plot the function
plt.stem(n, y)

# Customize x-axis ticks and labels
x_ticks = []
x_labels = []
plt.xticks(x_ticks, x_labels)

# Customize y-axis ticks and labels
y_ticks = []
y_labels = []
plt.yticks(y_ticks, y_labels)

# Set a title for the plot
plt.title('h[n]')

# Add x = 0
plt.axvline(0, color='black', linewidth=0.5)

# Disable the frame
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_visible(False)

ax.spines['bottom'].set_position('zero')

ax.text(-0.02, -0.02, '0', ha='right', va='center')

# Add text to the right of the x-axis
ax.text(3*np.pi+0.8, 0, 'n', ha='left', va='center')

# Display the plot
plt.show()