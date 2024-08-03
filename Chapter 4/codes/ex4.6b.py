import numpy as np
import matplotlib.pyplot as plt

# Define the continuous-time impulse function
def impulse(ω):
    # Create an array of zeros with the same shape as ω
    y = np.zeros_like(ω)
    
    # Set the value to 1 when t is close to 0
    epsilon = 1e-3  # A small positive value
    y[np.abs(ω) < epsilon] = 1

    return y

# T = 4 and T_1 = 1

# Define the range
ω = np.linspace(-10 , 10 , 200000)

y = 0
z = np.pi * np.sin(ω) / ω

for k in range(1, 6, 1):
    y += 2 * np.sin(0.5*k*np.pi) * impulse(ω-0.5*k*np.pi) / k

y += np.pi * impulse(ω)

for k in range(-5, 0, 1):
    y += 2 * np.sin(0.5*k*np.pi) * impulse(ω-0.5*k*np.pi) / k

# Plot the function
plt.plot(ω, y)
plt.plot(ω, z, '--')

# Customize x-axis ticks and labels
x_ticks = [-3 * np.pi, -2.5 * np.pi, -2 * np.pi, -1.5 * np.pi, -np.pi, -0.5 * np.pi, 0, 0.5 * np.pi, np.pi, 1.5 * np.pi, 2 * np.pi, 2.5 * np.pi, 3 * np.pi]
x_labels = ['$-6\omega_0$', '$-5\omega_0$', '$-4\omega_0$', '$-3\omega_0$', '$-2\omega_0$', '$-\omega_0$', '0', '$\omega_0$', '$2\omega_0$', '$3\omega_0$', '$4\omega_0$', '$5\omega_0$', '$6\omega_0$']
plt.xticks(x_ticks, x_labels)

# Customize y-axis ticks and labels
y_ticks = [0, 2, np.pi]
y_labels = ['0', '2', 'π']
plt.yticks(y_ticks, y_labels)

# Set a title for the plot
plt.title('X(jω)')

# Add x = 0 and y = 0 axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.xlabel('ω', loc='right')

# Display the plot
plt.show()
