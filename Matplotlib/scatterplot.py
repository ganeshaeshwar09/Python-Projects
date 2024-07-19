import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(1,20, 10)
y = [i ** 2 for i in x]

plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()