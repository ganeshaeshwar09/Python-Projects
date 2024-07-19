import matplotlib.pyplot as plt
import numpy as np

x = range(0, 11)
y = [2 * x for x in x]

plt.figure()
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('line graph: y = 2x')
plt.grid(True)
plt.show()
