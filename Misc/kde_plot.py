import seaborn as sns
import matplotlib.pyplot as plt

# Example data
data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 7]

# Create a KDE plot
sns.kdeplot(data, shade=True)

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('KDE Plot')

# Show the plot
plt.show()
