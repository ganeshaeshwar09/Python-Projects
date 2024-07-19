import pandas as pd
data1 = {
    'Name': ['Ganesh', 'Anil'],
    'Age': [10, 20]
}

df1 = pd.DataFrame(data1)


data2 = {
    'Name': ['Anil', 'uday'],
    'Age': [20, 30]
}
df2 = pd.DataFrame(data2)

merged_data = df1.merge(df2, on='Age', how ='inner')

print(merged_data)