import numpy as np
import matplotlib.pyplot as plt

x = [-np.pi, np.pi]
y = [-2*np.pi, 2*np.pi]

# Create a figure with a specific size (width, height) in inches
plt.figure(figsize=(6, 4))

# Plot the function
plt.plot(x, y)

# Customize x-axis ticks and labels
x_ticks = [-np.pi, np.pi]
x_labels = ['$-\pi$', '$\pi$']
plt.xticks(x_ticks, x_labels)

# Customize y-axis ticks and labels
y_ticks = [-2*np.pi, 2*np.pi]
y_labels = ['$-2\pi$', '$2\pi$']
plt.yticks(y_ticks, y_labels)

# Set a title for the plot
plt.title('$\sphericalangle X(e^{j\omega})$')

# Add x = 0 and y = 0 axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Disable the frame
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_visible(False)

ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

# Add text to the right of the x-axis
ax.text(np.pi+0.4, 0, '$\omega$', ha='left', va='center')

# Display the plot
plt.show()