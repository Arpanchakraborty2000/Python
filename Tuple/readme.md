# 📘 Python Tuple

A **tuple in Python** is a built-in data type that is used to store multiple items in a single variable, similar to a **list**, but with one key difference:

👉 **Tuples are immutable**, meaning once created, you cannot change, add, or remove elements from them.

---

## 🔹 Features of Tuple
- **Ordered** → Elements have a defined order, and that order will not change.  
- **Immutable** → Cannot be modified after creation (unlike lists).  
- **Allow duplicates** → Tuples can contain duplicate values.  
- **Can store mixed data types** → Integers, strings, lists, other tuples, etc.  
- **Indexed** → Elements can be accessed using index numbers `[0], [1], [2]...`.  

---

## 🔹 Creating Tuples

```python
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


# Accessing Tuple Elements

my_tuple = ("a", "b", "c", "d")

print(my_tuple[0])   # First element: a
print(my_tuple[-1])  # Last element: d
print(my_tuple[1:3]) # Slicing → ('b', 'c')


# Tuple Operations

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



# Tuple Methods
my_tuple = (1, 2, 2, 3, 4)

# Count occurrences of an element
print(my_tuple.count(2))   # 2

# Get index of first occurrence
print(my_tuple.index(3))   # 3


# Output Example
Tuple: (1, 2, 3, 4, 5)
Mixed tuple: (1, 'Hello', 3.14, True)
Nested tuple: (1, (2, 3), [4, 5])
Single element tuple: (10,)
a
d
('b', 'c')
(1, 2, 3, 4, 5)
(1, 2, 3, 1, 2, 3)
True
True
3
2
3
