import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Birthdate': ['2000-01-01', '1990-05-15', '1985-12-30', '1975-07-20']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
#rint(df)

df['Birthdate'] = pd.to_datetime(df['Birthdate'])
df.set_index('Birthdate', inplace=True)
print(df)