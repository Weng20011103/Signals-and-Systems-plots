import numpy as np
import matplotlib.pyplot as plt

x = [-np.pi, -0.5*np.pi, -0.5*np.pi, 0.5*np.pi, 0.5*np.pi, np.pi]
y = [0, 3, 2, 2, 3, 0]

# Create a figure with a specific size (width, height) in inches
plt.figure(figsize=(12, 3))

# Plot the function
plt.plot(x, y)

# Customize x-axis ticks and labels
x_ticks = [-np.pi, -0.5*np.pi, 0, 0.5*np.pi, np.pi, 3.3]
x_labels = ['$-\pi$', '$-\dfrac{\pi}{2}$', '0', '$\dfrac{\pi}{2}$', '$\pi$', '$\omega$']
plt.xticks(x_ticks, x_labels)

# Customize y-axis ticks and labels
y_ticks = [2, 3]
y_labels = ['2', '3']
plt.yticks(y_ticks, y_labels)

# Set a title for the plot
plt.title('$|X(e^{j\omega})|$')

# Add x = 0 and y = 0 axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Disable the frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# Display the plot
plt.show()