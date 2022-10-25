import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
])

print(np.sort(a, axis=0))
print(np.sort(a, axis=None))
print(np.sort(a, axis=1))