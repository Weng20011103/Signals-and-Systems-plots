import numpy as np
import matplotlib.pyplot as plt

def unit_step(x):
  return np.where(x >= 0, 1, 0)

# Define the continuous-time impulse function
def impulse(x):
  # Create an array of zeros with the same shape as ω
  y = np.zeros_like(x)
    
  # Set the value to 1 when t is close to 0
  epsilon = 1e-3  # A small positive value
  y[np.abs(x) < epsilon] = 1

  return y

x = np.linspace(-2, 2, 10000)
y1 = unit_step(x+1)-unit_step(x-1)
y2 = -impulse(x+1)
y3 = -impulse(x-1)

fig, axs = plt.subplots(3, 1, figsize=(12, 6))

axs[0].plot(x, y1, label='u(t+1)-u(t-1)')
axs[1].plot(x, y2, label='$-\delta(t+1)$')
axs[2].plot(x, y3, label='$-\delta(t-1)$')

# Set common ylim for all subplots
common_ylim = (-1.5, 1.5)

for ax in axs:
  ax.axvline(0, color='black', linewidth=0.5)
  ax.set_ylim(common_ylim)

# Set common x-ticks and x-labels for all subplots
common_xticks = np.arange(-1, 2, 1)
common_xticklabels = [str(i) for i in common_xticks]
for ax in axs:
  ax.set_xticks(common_xticks)
  ax.set_xticklabels(common_xticklabels)

# Add legends to each subplot
for ax in axs:
  ax.legend()

axs[2].set_xlabel('t', loc='right')

plt.show()