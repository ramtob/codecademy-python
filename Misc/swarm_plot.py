import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Example DataFrame
data = pd.DataFrame({
    'Category': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Value': [1, 2, 3, 4, 5, 6, 7, 8, 9]
})

# Create a swarm plot
sns.swarmplot(x='Category', y='Value', data=data)

# Add labels and title
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Swarm Plot of Values by Category')

# Show the plot
plt.show()
