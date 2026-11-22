import numpy as np
temps = np.array([32, 35, 31, 29, 38, 40, 36])
print("Shape",temps.shape)
print("Size",temps.size)
print("Dtype",temps.dtype)
print("Dimension",temps.ndim)
fahrenheit = temps* 9/5 + 32
print("Conversion in Fahrenheit : " , fahrenheit)
print(np.arange(0,7))

points = np.linspace(0, 1, 5)
print("Days",points)