import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['Ganesh', 'Anil'],
    'Score': [90, 80]
}

df = pd.DataFrame(data)

print(df)

df.plot(kind='bar', x='Name', y='Score')

plt.xlabel('Name')
plt.ylabel('Score')
plt.title('Score of Students')

plt.show()
