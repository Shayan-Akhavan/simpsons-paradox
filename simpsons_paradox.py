import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create synthetic data
np.random.seed(0)
size = 100
x = np.random.normal(50, 15, size)
y = 0.5 * x + np.random.normal(10, 10, size)

# Add group labels
group = np.random.choice(['A', 'B'], size)
data = pd.DataFrame({'x': x, 'y': y, 'group': group})

# Adjust y values for each group to create Simpson's Paradox
data.loc[data['group'] == 'A', 'y'] += 20
data.loc[data['group'] == 'B', 'y'] -= 20

# Scatter plot of both groups
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='x', y='y', hue='group')
plt.title("Scatter Plot by Group")
plt.show()

# Combined data scatter plot
plt.figure(figsize=(10, 6))
sns.regplot(data=data, x='x', y='y')
plt.title("Combined Data Scatter Plot")
plt.show()

# Regression lines for each group and combined
plt.figure(figsize=(10, 6))
sns.regplot(data=data[data['group'] == 'A'], x='x', y='y', label='Group A', color='b')
sns.regplot(data=data[data['group'] == 'B'], x='x', y='y', label='Group B', color='r')
sns.regplot(data=data, x='x', y='y', label='Combined', color='g')
plt.legend()
plt.title("Regression Lines by Group and Combined")
plt.show()
