import pandas as pd
filepath = r'C:\Users\ganes\OneDrive\Desktop\Python\Data\Excel_Sample.xlsx'
df = pd.read_excel(filepath)
print(df.head())