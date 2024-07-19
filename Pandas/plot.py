import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Score': [85, 90, 95, 80]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Plotting the 'Score' column as a bar chart
df.plot(kind='bar', x='Name', y='Score', legend=False)

# Adding labels and title
plt.xlabel('Name')
plt.ylabel('Score')
plt.title('Scores of Individuals')

# Display the plot
plt.show()