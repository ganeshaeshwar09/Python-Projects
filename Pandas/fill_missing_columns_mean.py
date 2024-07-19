import numpy as np
import pandas as pd
data = {
    "Name": ["raj", "ganesh", "anil"],
    "Age": [20, np.nan, 40],
    "city": ["bangalore", "hyd", "chennai"]
}

df  = pd.DataFrame(data)
print(df)

mean_age = df['Age'].mean()
mean_age = int(mean_age)
print("the mean age is :", mean_age)

df['Age'] = df['Age'].fillna(mean_age)

print("the data after filling missing values is:")
print(df)
