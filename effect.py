import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data
count_data = pd.read_csv('counts.csv')
outs_data = pd.read_csv('outs.csv')
bases_data = pd.read_csv('bases_occupied.csv')

# Example of visualizations
plt.figure(figsize=(12, 6))

# Plotting histograms for each dataset
plt.subplot(1, 3, 1)
sns.histplot(count_data['OBP'], bins=20, kde=True)
plt.title('Distribution of OBP by Count')
plt.xlabel('Split')  # Adjusted xlabel
plt.ylabel('OBP')

plt.subplot(1, 3, 2)
sns.barplot(data=outs_data, x='Split', y='OBP', palette='viridis')
plt.title('Distribution of OBP by Outs')
plt.xlabel('Outs')  # Adjusted xlabel
plt.ylabel('OBP')

plt.subplot(1, 3, 3)
sns.histplot(bases_data['OBP'], bins=20, kde=True)
plt.title('Distribution of OBP by Bases Occupied')
plt.xlabel('Split')  # Adjusted xlabel
plt.ylabel('OBP')

plt.tight_layout()
plt.show()

# Calculate correlations
correlation_count = count_data[['Split', 'OBP']].corr()
correlation_outs = outs_data[['Split', 'OBP']].corr()
correlation_bases = bases_data[['Split', 'OBP']].corr()

print("Correlation between Split and OBP for Count data:\n", correlation_count)
print("Correlation between Split and OBP for Outs data:\n", correlation_outs)
print("Correlation between Split and OBP for Bases Occupied data:\n", correlation_bases)