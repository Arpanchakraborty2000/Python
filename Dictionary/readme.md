# 📘 Python Dictionary

A **dictionary in Python** is a built-in data type that stores data in the form of **key–value pairs**.  
It is similar to a real dictionary where you look up a **word (key)** and get its **meaning (value)**.

---

## 🔹 Features of Dictionary
- **Unordered** → Items do not have a fixed order (before Python 3.7 it was completely unordered, but from 3.7+, insertion order is preserved).  
- **Mutable** → You can change, add, or remove items.  
- **Indexed by keys** → Unlike lists (indexed by numbers), dictionaries use **keys** to access values.  
- **Keys must be unique and immutable** (strings, numbers, tuples).  
- **Values can be anything** (string, int, list, another dictionary, etc.).

---

## 🔹 Example Code with Dictionary Methods

```python
# Creating dictionary
my_dict = {
    "name": "Arpan",
    "age": 25,
    "city": "Kolkata"
}
print("Original Dictionary:", my_dict)

# 1. get() → Get value by key (returns None if not found)
print("Name:", my_dict.get("name"))
print("Gender:", my_dict.get("gender", "Not Found"))

# 2. keys() → All keys
print("Keys:", my_dict.keys())

# 3. values() → All values
print("Values:", my_dict.values())

# 4. items() → All key-value pairs
print("Items:", my_dict.items())

# 5. update() → Update dictionary with another dict
my_dict.update({"age": 26, "country": "India"})
print("After update:", my_dict)

# 6. copy() → Shallow copy
copy_dict = my_dict.copy()
print("Copy of dictionary:", copy_dict)

# 7. pop() → Remove key and return value
age = my_dict.pop("age")
print("Popped age:", age)
print("After pop:", my_dict)

# 8. popitem() → Remove last inserted key-value pair
last_item = my_dict.popitem()
print("Popped last item:", last_item)
print("After popitem:", my_dict)

# 9. setdefault() → Return value if key exists, else insert with default value
country = my_dict.setdefault("country", "India")
print("Setdefault country:", country)
print("After setdefault:", my_dict)

# 10. fromkeys() → Create new dict from keys with same value
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print("New dict from keys:", new_dict)

# 11. clear() → Remove all items
temp = my_dict.copy()
temp.clear()
print("After clear:", temp)

# ------------------------------
# Extra Usage
# ------------------------------

# 12. in / not in → Check key existence
print("Is 'name' in dictionary?", "name" in my_dict)
print("Is 'salary' not in dictionary?", "salary" not in my_dict)

# 13. len() → Number of items
print("Length of dictionary:", len(my_dict))

# 14. dict comprehension → Create dict from expression
squares = {x: x**2 for x in range(5)}
print("Squares dictionary:", squares)
