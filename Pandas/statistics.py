import pandas as pd
filepath = r'C:\Users\ganes\OneDrive\Desktop\Python\Data\Details.txt'
df = pd.read_csv(filepath)
print(df)
print("The shape of the data frame is:", df.shape)
print("The statistics of the data frame is:", df.describe())