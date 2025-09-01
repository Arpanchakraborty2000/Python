# In Python, a set is a built-in data type that is used to store multiple items in a single variable.

## Think of it like a collection of unique values (no duplicates allowed).

## Key Points about set in Python:

## Unordered → The items don’t have a fixed order (so indexing/slicing doesn’t work).

## Unique Elements → Automatically removes duplicates.

## Mutable → You can add or remove elements after creating a set.

## Supports Mathematical Set Operations → union, intersection, difference, etc.


# Python Set Examples

This README contains **all important `set` methods in Python** with examples and outputs.

---

## 🔹 What is a Set?
- A **set** is an **unordered collection** of **unique elements**.
- Defined using `{}` or `set()` constructor.
- Supports **mathematical set operations** like union, intersection, difference, etc.

---

## 🔹 Full Example with All Set Methods

```python
# Creating sets
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print("s1 =", s1)
print("s2 =", s2)

# 1. add() → Add single element
s1.add(10)
print("After add:", s1)

# 2. update() → Add multiple elements
s1.update([20, 30])
print("After update:", s1)

# 3. remove() → Remove element (Error if not found)
s1.remove(10)
print("After remove:", s1)

# 4. discard() → Remove element (No error if not found)
s1.discard(100)   # No error
print("After discard:", s1)

# 5. pop() → Remove and return random element
popped = s1.pop()
print("Popped element:", popped)
print("After pop:", s1)

# 6. clear() → Remove all elements
temp = s1.copy()   # keep backup
temp.clear()
print("After clear:", temp)

# 7. copy() → Shallow copy of set
copy_s2 = s2.copy()
print("Copy of s2:", copy_s2)

# ------------------------------
# 🔹 Set Operations
# ------------------------------

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# 8. union() or | → Combine sets
print("Union:", s1.union(s2))
print("Union (|):", s1 | s2)

# 9. intersection() or & → Common elements
print("Intersection:", s1.intersection(s2))
print("Intersection (&):", s1 & s2)

# 10. difference() or - → Elements in s1 but not in s2
print("Difference (s1 - s2):", s1.difference(s2))
print("Difference (-):", s1 - s2)

# 11. symmetric_difference() or ^ → Elements not common
print("Symmetric Difference:", s1.symmetric_difference(s2))
print("Symmetric Difference (^):", s1 ^ s2)

# 12. issubset() → Checks if s1 is subset of s2
print("s1 issubset s2:", s1.issubset(s2))

# 13. issuperset() → Checks if s1 is superset of s2
print("s1 issuperset s2:", s1.issuperset(s2))

# 14. isdisjoint() → Checks if two sets have no elements in common
print("s1 isdisjoint {7, 8}:", s1.isdisjoint({7, 8}))
print("s1 isdisjoint s2:", s1.isdisjoint(s2))

# ------------------------------
# 🔹 Other Functions
# ------------------------------

# 15. len() → Number of elements
print("Length of s1:", len(s1))

# 16. in / not in → Membership
print("Is 2 in s1?", 2 in s1)
print("Is 10 not in s1?", 10 not in s1)
```

---

## 🔹 Sample Output

```
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
After add: {1, 2, 3, 4, 10}
After update: {1, 2, 3, 4, 10, 20, 30}
After remove: {1, 2, 3, 4, 20, 30}
After discard: {1, 2, 3, 4, 20, 30}
Popped element: 1
After pop: {2, 3, 4, 20, 30}
After clear: set()
Copy of s2: {3, 4, 5, 6}
Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Difference (s1 - s2): {1, 2}
Symmetric Difference: {1, 2, 5, 6}
s1 issubset s2: False
s1 issuperset s2: False
s1 isdisjoint {7, 8}: True
s1 isdisjoint s2: False
Length of s1: 4
Is 2 in s1? True
Is 10 not in s1? True
```

---

✅ Now you have a **complete README with all set methods in Python** 🚀
