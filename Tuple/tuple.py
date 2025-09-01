# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Tuple with mixed data types
mixed_tuple = (1, "Hello", 3.14, True)
print("Mixed tuple:", mixed_tuple)

# Nested tuple
nested_tuple = (1, (2, 3), [4, 5])
print("Nested tuple:", nested_tuple)

# Single element tuple (note the comma!)
single_tuple = (10,)
print("Single element tuple:", single_tuple)


my_tuple = ("a", "b", "c", "d")

print(my_tuple[0])   # First element: a
print(my_tuple[-1])  # Last element: d
print(my_tuple[1:3]) # Slicing → ('b', 'c')


tuple1 = (1, 2, 3)
tuple2 = (4, 5)

# Concatenation
print(tuple1 + tuple2)   # (1, 2, 3, 4, 5)

# Repetition
print(tuple1 * 2)        # (1, 2, 3, 1, 2, 3)

# Membership
print(2 in tuple1)       # True
print(6 not in tuple1)   # True

# Length
print(len(tuple1))       # 3
