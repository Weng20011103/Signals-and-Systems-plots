import numpy as np
import matplotlib.pyplot as plt

def f(x, N):
    # Create an array of zeros with the same shape as x
    y = np.zeros_like(x)
    
    # Set the value to 2*np.pi/N when x is close to 0
    epsilon = 1e-3  # A small positive value
    y[np.abs(x) < epsilon] = 2 * np.pi / N

    return y

N = 10

x = np.linspace(-10, 10, 50000)

y =  f(x+4*np.pi/N, N) + f(x+2*np.pi/N, N) + f(x, N) + f(x-2*np.pi/N, N) + f(x-4*np.pi/N, N)

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
x_ticks = [-4*np.pi/N, -2*np.pi/N, 0, 2*np.pi/N, 4*np.pi/N]
x_labels = ['$-\dfrac{4\pi}{N}$', '$-\dfrac{2\pi}{N}$', '0', '$\dfrac{2\pi}{N}$', '$\dfrac{4\pi}{N}$']
plt.xticks(x_ticks, x_labels)

# Customize y-axis ticks and labels
y_ticks = [0, 2*np.pi/N]
y_labels = ['0', '$2\pi/N$']
plt.yticks(y_ticks, y_labels)

# Set a title for the plot
plt.title('$X(e^{j\omega})$')

# Disable the frame
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_visible(False)

ax.spines['bottom'].set_position('zero')

# Add text to the right of the x-axis
ax.text(4*np.pi/N+0.01, 0, '$\omega$', ha='left', va='center')

plt.axvline(0, color='black', linewidth=0.5)

# Display the plot
plt.show()
