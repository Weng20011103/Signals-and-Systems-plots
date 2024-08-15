import numpy as np
import matplotlib.pyplot as plt

def x(n):
    return np.where(n >= -2, np.where(n <= 2, 1, 0), 0)

x = np.arange(-1, 12, 1)
y = [0, 0, 2 , 0, 2, 0, 2, 0, 2, 0, 2, 0, 0]

# Create a figure with a specific size (width, height) in inches
plt.figure(figsize=(12, 3))

plt.stem(x, y)
plt.title('$2y_{(2)}[n-1]$')
plt.grid(False)

xticks= np.arange(0, 10, 1)
xlabels = [str(i) for i in xticks]
xticks = np.append(xticks, 11)
xlabels = np.append(xlabels, 'n')
# Set x-axis labels to use the values from n
plt.xticks(xticks, labels=xlabels)

yticks= [0, 1, 2]
# Set y-axis labels to use the values from y_ticks
plt.yticks(yticks, labels=[str(i) for i in yticks])

# Disable the frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.show()
