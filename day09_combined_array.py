import numpy as np
arr1 = np.array([1,2,3,4,5]) #array 1
arr2 = np.array([6,7,8,9,10,11]) #array 2

#concatenate array1 with array2
combined = np.concatenate((arr1 , arr2))  #combine array with concatenate method
print(combined)

#compatibility of array
print("Compatibility shape " , arr1.shape == arr2.shape)
