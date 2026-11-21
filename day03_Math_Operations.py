import numpy as np

integers = np.array([1.28262 , 9.45363 , 7.65473])
prices = np.array([100, 250, 80, 400]) 
discount = discount = np.array([10, 25, 8, 40])
num = np.array([-10 , 8 , 9])
sales = np.array([[10, 12, 8],               
                  [5,  7,  6],               
                  [20, 18, 25],              
                  [2,  3,  4]])              

print("10 percent increase in prices" , prices * 1.10)
print("Rs. 20 decrease in price of every items" , prices - 20)
print("Square of prices", prices ** 2)
print("final price", prices - discount)
print(prices / discount)
print(np.round(prices * 1.075, 1))
print(np.sqrt(prices))
print(np.abs(num))
print(np.round(np.array([1.54546 , 4.476465 , 8.46464]) , 2))