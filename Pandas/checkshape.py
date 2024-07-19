#import pandas as pd
#frame = [1,2,3,4,5],[4,5,6,7],[9]
##df = pd.DataFrame(frame)
#print(df)
#print("The shape of the data is:")
#print(df.shape)

import pandas as pd
filepath = r'C:\Users\ganes\OneDrive\Desktop\Python\Data\Details.txt'
df = pd.read_csv(filepath)
print(df)
print("The shape of the data frame is:", df.shape)



