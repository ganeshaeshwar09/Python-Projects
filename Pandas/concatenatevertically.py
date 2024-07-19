import pandas as pd
data1 = {
    'ID': [1, 2],
    'Name': ['Alice', 'Bob'],
    'Score': [85, 90]
}
df1 = pd.DataFrame(data1)
data2 = {
    'ID': [3, 4],
    'Name': ['Charlie', 'David'],
    'Score': [95, 80]
}
df2 = pd.DataFrame(data2)
concatenated_df = pd.concat([df1, df2])

print(concatenated_df)