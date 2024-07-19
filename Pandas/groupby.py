import pandas as pd
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Values': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

grouped_mean = df.groupby('Category')['Values'].mean()
df = pd.DataFrame(grouped_mean)
print(df)