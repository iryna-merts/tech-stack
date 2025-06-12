import csv
import numpy as np

array_first = np.loadtxt('matrix.txt', delimiter =',')
array_second = array_first.copy()

print (array_first)
print (array_second)