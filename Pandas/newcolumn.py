import pandas as pd

data = {
    'Name':['Anil','Ganesh','Uday'],
    'age' :[33,34,55],
    'City':['BLR','HYD','Pune']
}
df=pd.DataFrame(data)
random_sample = df.sample(n=2)
shuffled_df = df.sample(frac=1).reset_index(drop=True)
print(random_sample)