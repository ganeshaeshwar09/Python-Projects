import pandas as pd

# Sample data to create DataFrame with duplicates
data = {
    'ID': [1, 2, 3, 4, 1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35, 40, 25, 30, 35]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print the original DataFrame with duplicates
print("Original DataFrame:")
print(df)

# Remove duplicate rows
df_no_duplicates = df.drop_duplicates()

# Print the DataFrame after removing duplicates
print("\nDataFrame after removing duplicates:")
print(df_no_duplicates)