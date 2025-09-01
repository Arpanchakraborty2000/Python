import numpy as np

# Create an array
arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)

# ----------------------------
# Shape and Type Information
# ----------------------------
print("Shape:", arr.shape)       # (5,)
print("Dimension:", arr.ndim)    # 1
print("Data Type:", arr.dtype)   # int64 (or int32 on Windows)
print("Size (total elements):", arr.size)

# ----------------------------
# Reshaping
# ----------------------------
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\nMatrix:\n", matrix)
print("Reshape (3x2):\n", matrix.reshape(3, 2))

# ----------------------------
# Indexing and Slicing
# ----------------------------
print("\nFirst element:", arr[0])
print("Last element:", arr[-1])
print("Slice [1:4]:", arr[1:4])
print("Step slicing [::2]:", arr[::2])

# ----------------------------
# Mathematical Operations
# ----------------------------
print("\nSum:", arr.sum())
print("Mean:", arr.mean())
print("Max:", arr.max())
print("Min:", arr.min())
print("Standard Deviation:", arr.std())
print("Cumulative Sum:", arr.cumsum())

# ----------------------------
# Array Methods
# ----------------------------
print("\nFlatten array:", matrix.flatten())
print("Transpose:\n", matrix.T)
print("Ravel (flatten view):", matrix.ravel())

# ----------------------------
# Creating Special Arrays
# ----------------------------
print("\nZeros:\n", np.zeros((2, 3)))
print("Ones:\n", np.ones((2, 3)))
print("Identity matrix:\n", np.eye(3))
print("Arange 0-9:", np.arange(10))
print("Linspace 0-1:", np.linspace(0, 1, 5))
print("Random values (0-1):\n", np.random.rand(2, 3))
print("Random integers:\n", np.random.randint(1, 10, (2, 3)))

# ----------------------------
# Boolean Operations
# ----------------------------
bool_arr = arr > 2
print("\nBoolean array:", bool_arr)
print("Values > 2:", arr[bool_arr])

# ----------------------------
# Stacking Arrays
# ----------------------------
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("\nVertical Stack:\n", np.vstack((a, b)))
print("Horizontal Stack:", np.hstack((a, b)))

# ----------------------------
# Copy vs View
# ----------------------------
copy_arr = arr.copy()
view_arr = arr.view()
arr[0] = 100
print("\nOriginal after change:", arr)
print("Copy (independent):", copy_arr)
print("View (shares data):", view_arr)
