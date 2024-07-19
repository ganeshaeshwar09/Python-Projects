import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(0, 100, 1000)

plt.hist(x, bins=20, color='blue', edgecolor='black')

plt.show()
