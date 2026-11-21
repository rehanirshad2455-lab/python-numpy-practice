import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])
print("Slicing : " , arr[2 : 8])
print("With steps " ,arr[0:8:2])
print("Negative indexing :" ,arr[-2])

#2d arrays==================================
arr_2d = np.array([[1,2,3],[4,5,6]])
print("specific element :" , arr_2d[1 , 0])
print("Entire Row : " , arr_2d[1])
print("Entire Column : "  , arr_2d[:,1])

#=====Sorting==================================

unsorted = np.array([1,5,4,6,7,9,3,22,4,5,7,9,9,10,1])
print("Sorted Array : ", np.sort(unsorted))

#================= Sorting in 2D=============
arr_2d_unsorted = np.array([[4,1,3,2], [5,7,6,8]])
print("Sorting in 2d array" ,np.sort(arr_2d_unsorted , axis = 1))