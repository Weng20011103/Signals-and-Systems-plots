import numpy as np
import matplotlib.pyplot as plt

def y(x):
  # Create an array of zeros with the same shape as x
    y = np.zeros_like(x)
    
    # Apply the piecewise conditions
    y[x < -2] = 0
    y[(-2 <= x) & (x < 0)] = 1 / (2 * np.pi)
    y[(0 < x) & (x <= 2)] = -1 / (2 * np.pi)
    y[x > 2] = 0
    
    return y

x = np.linspace(-30, 30, 10000)
y1 = x * (np.sin(x) / (np.pi * x))**2
y2 = y(x)

fig, axs = plt.subplots(2, 1, figsize=(12, 4))

axs[0].plot(x, y1, label=r'$t\cdot\left(\dfrac{\sin(t)}{\pi t}\right)^2$')
axs[1].plot(x, y2, label=r'$X(j\omega)$')

# Set ylim to each subplot
axs[0].set_ylim(-0.1, 0.1)
axs[1].set_ylim(-0.2, 0.2)

axs[0].axhline(0, color='black', linewidth=0.5)

for ax in axs:
  ax.axvline(0, color='black', linewidth=0.5)

# Customize x-axis ticks and labels
x_ticks = [-3*np.pi, -2*np.pi, -np.pi, 0, np.pi, 2*np.pi, 3*np.pi, 30]
x_labels = ['$-3\pi$', '$-2\pi$', '$-\pi$', '0', '$\pi$', '$2\pi$', '$3\pi$', 't']
axs[0].set_xticks(x_ticks)
axs[0].set_xticklabels(x_labels)

x_ticks = [-2, 2, 30]
x_labels = ['-2', '2', '$\omega$']
axs[1].set_xticks(x_ticks)
axs[1].set_xticklabels(x_labels)

# Customize y-axis ticks and labels
y_ticks = [0]
y_labels = ['0']
axs[0].set_yticks(y_ticks)
axs[0].set_yticklabels(y_labels)

y_ticks = [-1/(2*np.pi), 0, 1/(2*np.pi)]
y_labels = ['$-\dfrac{j}{2\pi}$', '0', '$\dfrac{j}{2\pi}$']
axs[1].set_yticks(y_ticks)
axs[1].set_yticklabels(y_labels)

# Add legends to each subplot
for ax in axs:
  ax.legend()

plt.show()