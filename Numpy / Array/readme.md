# 📊 NumPy Arrays in Python

NumPy (**Numerical Python**) is a powerful Python library for numerical computations.  
It provides the `ndarray` object – a fast, flexible, and memory-efficient array structure.

---

## 🔹 Why NumPy Arrays?
- Faster than Python lists
- Supports **multi-dimensional arrays**
- Provides **vectorized operations**
- Rich set of **mathematical & statistical functions**
- Useful in **Data Science, Machine Learning, AI, and Scientific Computing**

---

## 🔹 Creating NumPy Arrays

```python
import numpy as np

# From Python list
arr = np.array([1, 2, 3, 4, 5])

# Multi-dimensional array
arr2d = np.array([[1,2,3], [4,5,6]])

# Using arange
arr_range = np.arange(0, 10, 2)   # [0,2,4,6,8]

# Using linspace
arr_lin = np.linspace(0, 1, 5)    # [0., 0.25, 0.5, 0.75, 1.]

# Zeros and Ones
zeros = np.zeros((2,3))
ones = np.ones((3,3))

# Identity matrix
eye = np.eye(4)

# Random values
rand = np.random.rand(3,3)

# Array Attributes

arr = np.array([[1,2,3],[4,5,6]])

print(arr.shape)   # (2, 3)
print(arr.ndim)    # 2 (2D array)
print(arr.size)    # 6 (total elements)
print(arr.dtype)   # int64 / float64


# Array Indexing & Slicing

arr = np.array([10,20,30,40,50])

print(arr[0])      # 10
print(arr[-1])     # 50
print(arr[1:4])    # [20,30,40]

arr2d = np.array([[1,2,3],[4,5,6]])
print(arr2d[0,1])  # 2
print(arr2d[:,2])  # [3,6]


# Array Reshaping

arr = np.arange(1, 11)

print(arr.reshape(2,5))   # 2x5 matrix
print(arr.reshape(5,2))   # 5x2 matrix
print(arr.reshape(-1,5))  # auto adjust rows

# Array Operations

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)   # [5,7,9]
print(a - b)   # [-3,-3,-3]
print(a * b)   # [4,10,18]
print(a / b)   # [0.25,0.4,0.5]
print(a ** 2)  # [1,4,9]

# Useful Functions

arr = np.array([1,2,3,4,5])

print(np.min(arr))     # 1
print(np.max(arr))     # 5
print(np.sum(arr))     # 15
print(np.mean(arr))    # 3.0
print(np.std(arr))     # Standard deviation
print(np.sqrt(arr))    # Square root


# Random & Special Arrays

np.random.randint(1, 10, (3,3))   # Random integers
np.random.randn(2,4)              # Standard normal distribution
np.full((2,2), 7)                 # Fill with constant
np.eye(3)                         # Identity matrix


📌 Summary

NumPy arrays are faster and more efficient than lists.

Support powerful operations like reshaping, broadcasting, and vectorization.

Essential for Data Science, ML, AI, Image Processing, and Statistics.