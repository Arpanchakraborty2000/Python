import numpy as np 

lst = [1, 2, 3, 4, 5]      # A normal Python list
arr = np.array(lst)        # Convert list to NumPy array

print(arr)                 # Output: [1 2 3 4 5]
print(type(arr))           # Output: <class 'numpy.ndarray'>



####### 2D Array #########
print("######################################")



lst1 =[1,2,3,4,5]
lst2 =[5,2,3,4,5]
lst3 =[8,2,3,4,5]

arr = np.array([lst1,lst2,lst3])
print(arr)
print(arr.shape) ## this will provide how many row and column in present in this array


## Array index wise call -----------

arr = [1,2,3,4,5]
print(np.array(arr[2]))
print(type(np.array(arr)))

## value change -----------

arr[2] = 9
print("new value of this : ",np.array(arr[2]))
print("particular value of this array ",np.array(arr[1:4]))


