import pandas as pd

data = {
    'Date': ['2023-01-01', '2023-02-01', '2023-03-01'],
    'Item_A': [100, 200, 300],
    'Item_B': [150, 250, 350]
}
df_wide = pd.DataFrame(data)

print("Original Wide DataFrame:")
print(df_wide)

df_long = pd.melt(df_wide, id_vars=['Date'], var_name='Item', value_name='Sales')

print(df_long)