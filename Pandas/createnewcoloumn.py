import pandas as pd
data = {
    'coloumn1': [1,2,3],
    'coloumn2': [4,5,6]
}

df = pd.DataFrame(data)

df['New Coloumn'] = df['coloumn1']+df['coloumn2']

df.rename(columns={'New Coloumn':'Sum column'}, inplace=True)

print(df)