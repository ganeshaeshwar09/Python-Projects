import pandas as pd

data = {
    'name':('Anil','Ganesh','Uday'),
    'age':(22,33,44),
    'Location':('Hyd','Blr','Chennai')
    }
df = pd.DataFrame(data)
print(df)
age = df[df['age'] > 25]
print(age)