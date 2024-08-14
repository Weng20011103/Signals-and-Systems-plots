import numpy as np
import matplotlib.pyplot as plt

def x(n, W):
    return np.where(n == 0, W / np.pi, np.sin(W*n) / (np.pi*n))

# Generate a range of n values
n = np.arange(-10, 11, 1)

y1 = x(n, np.pi/4)
y2 = x(n, 3*np.pi/8)
y3 = x(n, np.pi/2)
y4 = x(n, 3*np.pi/4)
y5 = x(n, 7*np.pi/8)
y6 = x(n, np.pi)

fig, axs = plt.subplots(6, 1, figsize=(12, 15))

axs[0].stem(n, y1, label='$W=\pi/4$')
axs[1].stem(n, y2, label='$W=3\pi/8$')
axs[2].stem(n, y3, label='$W=\pi/2$')
axs[3].stem(n, y4, label='$W=3\pi/4$')
axs[4].stem(n, y5, label='$W=7\pi/8$')
axs[5].stem(n, y6, label='$W=\pi$')

xticks = [0]
xticklabels = [str(i) for i in xticks]
xticks = np.append(xticks, 10)
xticklabels = np.append(xticklabels, 'n')
# Set x-ticks only for the last subplot
axs[5].set_xticks(xticks, xticklabels)

# Hide x-ticks for other subplots
for ax in axs[:-1]:
    ax.set_xticks([])

# Add legends to each subplot
for ax in axs:
  ax.legend()

# Add subtitles to subplot
axs[0].set_title(r'$\tilde{x}[n]$')

# Set different y-ticks for each subplot
axs[0].set_yticks([0, 0.25], ['0', '0.25'])
axs[1].set_yticks([0, 3/8], ['0', '0.375'])
axs[2].set_yticks([0, 0.5], ['0', '0.5'])
axs[3].set_yticks([0, 0.75], ['0', '0.75'])
axs[4].set_yticks([0, 7/8], ['0', '0.875'])
axs[5].set_yticks([0, 1], ['0', '1'])

plt.show()