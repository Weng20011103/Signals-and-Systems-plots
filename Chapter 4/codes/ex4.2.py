import numpy as np
import matplotlib.pyplot as plt

def x(t):
    # Create an array of zeros with the same shape as t
    y = np.zeros_like(t)
    
    # Apply the piecewise conditions
    y[t < 0] = np.e ** (t[t < 0])
    y[(4 <= t) & (t < 5)] = 0
    y[t > 0] = np.e ** (-t[t > 0])
    
    return y

def X(ω):
    a = 1
    # Create an array of zeros with the same shape as t
    y = 2 * a / (a**2 + ω**2)
    
    return y
    
# Define the time range
t = np.linspace(-10 , 10 , 10000)
# Define the frequency range
ω = np.linspace(-10 , 10 , 10000)

# Generate data for the subplots
y1 = x(t)
y2 = X(ω)

# Create a figure with 2 vertical subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 15))

# Plot data in each subplot
axs[0].plot(t, y1)
axs[1].plot(t, y2)

# Set x-ticks for other subplots
for ax in axs[:-1]:
    ax.set_xticks(np.arange(-10, 11, 1))

# Set x-ticks 
x_ticks = [-1, 1]
x_labels = ['-a', 'a']

# Set x-ticks only for the last subplot
axs[1].set_xticks(x_ticks, x_labels)

# Set y-ticks 
y_ticks = [1, 2]
y_labels = ['1/a', '2/a']

# Set y-ticks only for the last subplot
axs[1].set_yticks(y_ticks, y_labels)

# Set different title for each subplot
axs[0].set_title('x(t)')
axs[1].set_title('X(jω)')

# Add the vertical lines at ω = 1 and ω = -1
axs[1].axvline(x=-1, ymin=-1, ymax=0.5, color='black', linestyle='--')
axs[1].axvline(x=1, ymin=-1, ymax=0.5, color='black', linestyle='--')
# Add the horizontal lines at y = 1
axs[1].axhline(y=1, xmin=-1, xmax=0.545, color='black', linestyle='--')
axs[1].axhline(y=2, xmin=-1, xmax=0.5, color='black', linestyle='--')

# Adjust layout to prevent overlap
plt.tight_layout(h_pad = 5)

plt.show()