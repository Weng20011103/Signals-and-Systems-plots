import numpy as np
import matplotlib.pyplot as plt

def X(ω):
    T_1 = 1
    # Create an array of zeros with the same shape as ω
    y = 2 * np.sin(ω * T_1) / ω
    
    return y

# Define the frequency range
ω = np.linspace(-20 , 20 , 10000)

y = X(ω)

# Plot the function
plt.plot(ω, y)

# Customize x-axis ticks and labels
x_ticks = [-6 * np.pi, -5 * np.pi, -4 * np.pi, -3 * np.pi, -2 * np.pi, -np.pi, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi, 5 * np.pi, 6 * np.pi]
x_labels = ['$-\dfrac{6π}{T_1}$', '$-\dfrac{5π}{T_1}$', '$-\dfrac{4π}{T_1}$', '$-\dfrac{3π}{T_1}$', '$-\dfrac{2π}{T_1}$', '-$\dfrac{π}{T_1}$', '$\dfrac{π}{T_1}$', '$\dfrac{2π}{T_1}$', '$\dfrac{3π}{T_1}$', '$\dfrac{4π}{T_1}$', '$\dfrac{5π}{T_1}$', '$\dfrac{6π}{T_1}$']
plt.xticks(x_ticks, x_labels)

# Customize y-axis ticks and labels
y_ticks = [0, 2]
y_labels = ['0', '2$T_1$']
plt.yticks(y_ticks, y_labels)

# Set a title for the plot
plt.title('X(jω)')

# Add x = 0 and y = 0 axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Display the plot
plt.show()
