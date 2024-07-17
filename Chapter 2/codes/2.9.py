import numpy as np
import matplotlib.pyplot as plt

# Define the continuous-time unit step function
def u(t):
    return np.where(t >= 0, 1, 0)

def h(t):
    # Create an array of zeros with the same shape as t
    y = np.zeros_like(t)
    
    # Apply the piecewise conditions
    y[t < 4] = np.e ** (2*t[t < 4])
    y[(4 <= t) & (t < 5)] = 0
    y[t > 5] = np.e ** (-2*t[t > 5])
    
    return y
    
# Define the time range
t = np.linspace(-10 , 10 , 10000)

# Generate data for the subplots
y1 = h(t)
y2 = h(-t)
y3 = h(5-t)

# Create a figure with 3 vertical subplots
fig, axs = plt.subplots(3, 1, figsize=(8, 15))

# Plot data in each subplot
axs[0].plot(t, y1)
axs[1].plot(t, y2)
axs[2].plot(t, y3)

# Set x-ticks for other subplots
for ax in axs[:-1]:
    ax.set_xticks(np.arange(-10, 11, 1))

# Set x-ticks 
x_ticks = [0, 1]
x_labels = ['t-5', 't-4']

# Set x-ticks only for the last subplot
axs[2].set_xticks(x_ticks, x_labels)

# Set different title for each subplot
axs[0].set_title('h(τ)')
axs[1].set_title('h(-τ)')
axs[2].set_title('h(t-τ), t=5')

# Adjust layout to prevent overlap
plt.tight_layout(h_pad = 5)

plt.show()