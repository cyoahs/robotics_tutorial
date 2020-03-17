import numpy as np

a = np.arange(12).reshape([3, 4])

b = np.arange(8).reshape([4, 2])
# martix multiplication
c = np.matmul(a, b)
# element-wise multiplication
d = a*a
# bool index
d[a > 6] = 0
# sin
np.sin(a)
# shape
a.shape
# concatenate
np.hstack((a, b))
np.vstack((a, b))

