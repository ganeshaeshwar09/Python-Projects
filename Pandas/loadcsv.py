import pandas as pd
filepath = r'C:\Users\ganes\OneDrive\Desktop\Python\Data\SeoulBikeData.csv'
df = pd.read_csv(filepath, encoding='ISO-8859-1')
print(df)
