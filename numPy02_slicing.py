import numpy as np

arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

print(arr[0:2 , 0:2])
print(arr[2:4 , 2:4])
print(arr[:, 1])
print(arr[2,:])
print(arr[0:3 , 1:3])