#1
import numpy as np

arr = np.array([1, 2, 3, 6, 4, 5])
reversed_arr = arr[::-1]
print(reversed_arr)

#2
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [3, 4]])

result = np.array_equal(arr1, arr2)
print(result) 

#3
import numpy as np

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])


mode_x = np.bincount(x).argmax()
indices_x = np.where(x == mode_x)[0]
print("Most frequent value in x:", mode_x)
print("Indices of most frequent value(s) in x:", indices_x)


mode_y = np.bincount(y).argmax()
indices_y = np.where(y == mode_y)[0]
print("Most frequent value in y:", mode_y)
print("Indices of most frequent value(s) in y:", indices_y)


#4

import numpy as np

gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')

# Sum of all elements
total_sum = np.sum(gfg)

# Sum row-wise
row_sum = np.sum(gfg, axis=1)

# Sum column-wise
col_sum = np.sum(gfg, axis=0)

print("Sum of all elements=", total_sum)
print("Sum of all elements row-wise=", row_sum)
print("Sum of all elements column-wise=", col_sum)

