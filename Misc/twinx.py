import matplotlib.pyplot as plt

# Example data
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
y2 = [1, 4, 9, 16, 25]

# Create a plot with the first y-axis
fig, ax1 = plt.subplots()
ax1.plot(x, y1, 'g-')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y1-axis', color='g')

# Create a second y-axis sharing the same x-axis
ax2 = ax1.twinx()
ax2.plot(x, y2, 'b-')
ax2.set_ylabel('Y2-axis', color='b')

# Show the plot
plt.title('Plot with Two Y-Axes')
plt.show()
