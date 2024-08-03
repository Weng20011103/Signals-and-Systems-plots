import numpy as np
import matplotlib.pyplot as plt

def X(ω):
    W = 1
    # Create an array of zeros with the same shape as ω
    y = np.zeros_like(ω)
    
    # Apply the piecewise conditions
    y[ω < -W] = 0
    y[(-W <= ω) & (ω < W)] = 1
    y[ω > W] = 0
    
    return y

# Define the time range
ω = np.linspace(-6, 6, 10000)

y = X(ω)

# Plot the function
plt.plot(ω, y)

# Customize x-axis ticks and labels
x_ticks = [-1, 1]
x_labels = ['-W', 'W']
plt.xticks(x_ticks, x_labels)

# Customize y-axis ticks and labels
y_ticks = [0, 1]
y_labels = ['0', '1']
plt.yticks(y_ticks, y_labels)

# Set the ylim
plt.ylim(-0.1, 1.3)

# Set a title for the plot
plt.title('X(jω)')

# Add x = 0 and y = 0 axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.xlabel('ω', loc='right')

# Display the plot
plt.show()
