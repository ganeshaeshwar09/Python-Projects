import matplotlib.pyplot as plt
import numpy as np

scores_range = ['0-25', '25-50', '50-75', '75-100']
students_in_range = [15, 20, 30, 10]

plt.bar(scores_range, students_in_range, color='blue', edgecolor='black')
plt.xlabel('Score')
plt.ylabel('Students_in_range')
plt.title('Scorecard')
plt.show()