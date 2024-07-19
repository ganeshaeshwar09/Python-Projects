import pandas as pd

data = {
    'Name':['Anil','Ganesh','Uday'],
    'age' :[33,34,55],
    'location':['BLR','HYD','Pune']
}
df=pd.DataFrame(data)
print(df)

df.to_csv('output2024.csv')

print('Scuesfflly comeplted output')

import pandas as pd

data = {
    'Name':['Anil','Ganesh','Uday'],
    'age' :[33,34,55],
    'location':['BLR','HYD','Pune']
}
df=pd.DataFrame(data)
print(df)

df.to_excel('output2024.xlsx')