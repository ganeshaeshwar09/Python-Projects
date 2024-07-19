import pandas as pd

data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-02-01', '2023-02-01', '2023-03-01', '2023-03-01'],
    'Item': ['Item_A', 'Item_B', 'Item_A', 'Item_B', 'Item_A', 'Item_B'],
    'Sales': [100, 150, 200, 250, 300, 350]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df['Date'] = pd.to_datetime(df['Date'])

pivoted_df = df.pivot(index='Date', columns='Item', values='Sales')

print(pivoted_df)