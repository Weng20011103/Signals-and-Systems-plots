import numpy as np
import matplotlib.pyplot as plt

# Define the continuous-time impulse function
def impulse(t):
    # Create an array of zeros with the same shape as t
    y = np.zeros_like(t)
    
    # Set the value to 1 when t is close to 0
    epsilon = 1e-3  # A small positive value
    y[np.abs(t) < epsilon] = 1

    return y

def x(t):
    # Create an array of zeros with the same shape as t
    y = np.zeros_like(t)
    
    # Apply the piecewise conditions
    y[t < 0] = 0
    y[(0 <= t) & (t < 1)] = t[(0 <= t) & (t < 1)] + 1
    y[(1 < t) & (t <= 2)] = 2 - t[(1 < t) & (t <= 2)]
    y[t > 2] = 0
    
    return y

def y(t):
    # Create an array of zeros with the same shape as t
    y = np.zeros_like(t)
    
    # Apply the piecewise conditions
    y[t <= -2] = 0
    y[(-2 < t) & (t <= -1)] = t[(-2 <= t) & (t < -1)] + 3
    y[(-1 < t) & (t <= 0)] = t[(-1 < t) & (t <= 0)] + 4
    y[(0 < t) & (t <= 1)] = 2 - 2 * t[(0 < t) & (t <= 1)]
    y[t > 1] = 0
    
    return y
    
# Define the time range and the sine function
t = np.linspace(-5 , 5 , 10000)  # Time from -5 to 5 with 10000 points

# Generate data for the subplots
y1 = x(t)
y2 = impulse(t+2) + 2 * impulse(t+1)
y3 = y(t)

# Create a figure with 3 vertical subplots
fig, axs = plt.subplots(3, 1, figsize=(8, 15))

# Plot data in each subplot
axs[0].plot(t, y1)
axs[1].plot(t, y2)
axs[2].plot(t, y3)

# Set x-ticks to multiples of pi/2
x_ticks = np.arange(-5, 5, 0.5)

# Set x-ticks for subplots
for ax in axs:
    ax.set_xticks(x_ticks)

# Set different title for each subplot
axs[0].set_title('x(t)')
axs[1].set_title('h(t)')
axs[2].set_title('y(t)')

# Adjust layout to prevent overlap
plt.tight_layout(h_pad = 5)

plt.show()