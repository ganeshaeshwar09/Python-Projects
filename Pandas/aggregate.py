import pandas as pd
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Values1': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Grouping by 'Category' and aggregating multiple statistics
aggregated_df = df.groupby('Category').agg({
    'Values1': ['mean', 'sum', 'count']
}).reset_index()
print(aggregated_df)