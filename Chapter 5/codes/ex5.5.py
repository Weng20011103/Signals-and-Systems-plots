import numpy as np
import matplotlib.pyplot as plt

def f(x, ω):
    # Create an array of zeros with the same shape as x
    y = np.zeros_like(x)
    
    # Set the value to np.pi when x is close to ω and -ω
    epsilon = 1e-3  # A small positive value
    y[np.abs(x-ω) < epsilon] = np.pi
    y[np.abs(x+ω) < epsilon] = np.pi

    return y

ω = np.pi/4

x = np.linspace(-10, 10, 50000)

y = f(x+2*np.pi, ω) + f(x, ω) + f(x-2*np.pi, ω)

# Filter out the points where y is 0
x_filtered = x[y != 0]
y_filtered = y[y != 0]

# Create a figure with a specific size (width, height) in inches
plt.figure(figsize=(12, 3))

# Plot the function with blue color
markerline, stemlines, baseline = plt.stem(x_filtered, y_filtered)
plt.setp(stemlines, linestyle="-", color="blue", linewidth=1)
plt.setp(markerline, marker='^', markersize=8, color='blue')

# Customize x-axis ticks and labels
x_ticks = [-2*np.pi-ω, -2*np.pi+ω, -ω, 0, ω, 2*np.pi-ω, 2*np.pi, 2*np.pi+ω]
x_labels = ['$(-2\pi-\omega_0)$', '$(-2\pi+\omega_0)$', '$-\omega_0$', '0', '$\omega_0$', '$(2\pi-\omega_0)$', '$2\pi$', '$(2\pi+\omega_0)$']
plt.xticks(x_ticks, x_labels)

# Customize y-axis ticks and labels
y_ticks = [0, np.pi]
y_labels = ['0', '$\\pi$']
plt.yticks(y_ticks, y_labels)

# Set a title for the plot
plt.title('$X(e^{j\omega})$')

# Disable the frame
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_visible(False)

ax.spines['bottom'].set_position('zero')

# Add text to the right of the x-axis
ax.text(7.2, -0.01, '$\omega$', ha='left', va='center')

plt.axvline(0, color='black', linewidth=0.5)

# Display the plot
plt.show()
