import numpy as np
t1 = np.array([
    [3,2,3],
    [1,4,5], 
    [7,6,8],
])

t2 = np.array([
    [1,2,3],
    [3,4,5], 
    [7,6,8],
])


if np.array_equal(t1,t2):
    print('son iguales')
print('no son iguales')