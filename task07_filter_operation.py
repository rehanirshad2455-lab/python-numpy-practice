import numpy as np
numbers = np.array([1,2,3,4,5,6,7,8,9,10])
even_numbers = numbers[numbers % 2== 0]
print(even_numbers)

print("------- Filter with mask--------")
mask = numbers > 5
print(numbers[mask])

indices = [0,1,2,3,4]
print(numbers[indices])

where_result = np.where(numbers > 5)
print("numbers which is greater than 5 is : " , numbers[where_result])