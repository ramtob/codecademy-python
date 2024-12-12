import matplotlib.pyplot as plt
import numpy as np

# Example data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])
yerr = np.array([0.5, 0.4, 0.6, 0.3, 0.5])  # Error values

# Create scatter plot with error bars
plt.errorbar(x, y, yerr=yerr, fmt='o', ecolor='r', capsize=5)

# Show the plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Error Bars')
plt.show()
