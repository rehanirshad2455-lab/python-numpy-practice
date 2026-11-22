import numpy as np
marks = np.array([[78, 85, 72, 66],
                  [90, 88, 95, 84],
                  [65, 70, 60, 58],
                  [82, 79, 88, 91]])
print("2nd student's 3rd Subject" , marks[1 , 2])
print("Last student's Marks" , marks[3] )
print("First Complete column" , marks[:, 0])
print("2 X 2 :",marks[1:3, 1:3])
print("Every 2nd row :\n",marks[::2])
print("All corner's elements" , marks[[0,0,3,3] , [0,3,0,3]]) 
new_matrix = marks.copy()
print("Copy of Matrix" , new_matrix)
new_matrix[0] = 0
print("new matrix" , new_matrix)
print("Original marks remain unchanged :\n",marks)