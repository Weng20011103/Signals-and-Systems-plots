import numpy as np
import matplotlib.pyplot as plt

def unit_step(x):
  return np.where(x >= 0, 1, 0)

x = np.linspace(-30, 30, 10000)
y1 = np.sin(x) / (np.pi * x)
y2 = unit_step(x+1) - unit_step(x-1)

fig, axs = plt.subplots(2, 1, figsize=(12, 4))

axs[0].plot(x, y1, label='$\dfrac{\sin(t)}{\pi t}$')
axs[1].plot(x, y2, label='$Y(j\omega)$')

# Set ylim to each subplot
axs[0].set_ylim(-0.2, 0.4)
axs[1].set_ylim(-0.1, 1.1)

axs[0].axhline(0, color='black', linewidth=0.5)

for ax in axs:
  ax.axvline(0, color='black', linewidth=0.5)

# Customize x-axis ticks and labels
x_ticks = [-3*np.pi, -2*np.pi, -np.pi, 0, np.pi, 2*np.pi, 3*np.pi, 30]
x_labels = ['$-3\pi$', '$-2\pi$', '$-\pi$', '0', '$\pi$', '$2\pi$', '$3\pi$', 't']
axs[0].set_xticks(x_ticks)
axs[0].set_xticklabels(x_labels)

x_ticks = [-1, 1, 30]
x_labels = ['-1', '1', '$\omega$']
axs[1].set_xticks(x_ticks)
axs[1].set_xticklabels(x_labels)

# Customize y-axis ticks and labels
y_ticks = [0, 1/np.pi]
y_labels = ['0', '$\dfrac{1}{\pi}$']
axs[0].set_yticks(y_ticks)
axs[0].set_yticklabels(y_labels)

y_ticks = [0, 1]
y_labels = ['0', '1']
axs[1].set_yticks(y_ticks)
axs[1].set_yticklabels(y_labels)

# Add legends to each subplot
for ax in axs:
  ax.legend()

plt.show()