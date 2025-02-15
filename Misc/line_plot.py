import matplotlib.pyplot as plt

# Example data
x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [0, 1, 2, 3, 4]

# Plot with different linestyles
plt.plot(x, y1, linestyle='-', label='Solid Line')
plt.plot(x, y2, linestyle='--', label='Dashed Line')

# Add labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Show the plot
plt.show()
