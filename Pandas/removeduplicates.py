import pandas as pd
frame = [1,2,3,4,5,6,5,7,3,2,1]
df = pd.DataFrame(frame)
#print(df)
df_no_duplicates = df.drop_duplicates()
print(df_no_duplicates)