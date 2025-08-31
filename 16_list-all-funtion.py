# Python List Methods Cheat Sheet
'''
Explanation of Functions

append() → Adds single item to end.

insert() → Inserts at given index.

extend() → Adds multiple items from another list.

remove() → Removes first match.

pop() → Removes by index (returns removed item).

clear() → Empties the list.

index() → Returns index of first match.

count() → Counts occurrences of an item.

sort() → Sorts in place.

reverse() → Reverses list order.

copy() → Copies list.

len() → Returns length.

max(), min(), sum() → Aggregate functions.

any(), all() → Boolean checks.

sorted() → Returns sorted copy without changing original.

list comprehension → Quick transformation.

slicing → Extracts sublists.
'''
# Sample list
numbers = [10, 20, 30, 40, 20]
fruits = ["apple", "banana", "cherry"]

print("Original numbers list:", numbers)
print("Original fruits list:", fruits)
print("="*50)

# 1. append() → Add element at the end
fruits.append("orange")
print("append():", fruits)

# 2. insert() → Insert at specific position
fruits.insert(1, "mango")
print("insert():", fruits)

# 3. extend() → Add elements from another list
fruits.extend(["grape", "kiwi"])
print("extend():", fruits)

# 4. remove() → Remove first matching element
fruits.remove("banana")
print("remove():", fruits)

# 5. pop() → Remove by index (default last)
removed_item = fruits.pop(2)
print("pop(): removed", removed_item, "=>", fruits)

# 6. clear() → Remove all elements
temp = fruits.copy()
temp.clear()
print("clear():", temp)

# 7. index() → Get index of first occurrence
print("index() of 20:", numbers.index(20))

# 8. count() → Count occurrences
print("count() of 20:", numbers.count(20))

# 9. sort() → Sort list (ascending / descending)
nums_copy = numbers.copy()
nums_copy.sort()
print("sort() ascending:", nums_copy)
nums_copy.sort(reverse=True)
print("sort() descending:", nums_copy)

# 10. reverse() → Reverse the list
nums_copy.reverse()
print("reverse():", nums_copy)

# 11. copy() → Shallow copy of list
new_list = numbers.copy()
print("copy():", new_list)

# 12. len() → Length of list
print("len(numbers):", len(numbers))

# 13. max() → Largest element
print("max(numbers):", max(numbers))

# 14. min() → Smallest element
print("min(numbers):", min(numbers))

# 15. sum() → Sum of elements
print("sum(numbers):", sum(numbers))

# 16. List comprehension → Short way to create new list
squares = [x**2 for x in numbers]
print("List comprehension (squares):", squares)

# 17. any() → True if at least one element is True
print("any([0, False, 5]):", any([0, False, 5]))

# 18. all() → True if all elements are True
print("all([1, 2, 3]):", all([1, 2, 3]))

# 19. sorted() → Returns new sorted list (doesn't change original)
print("sorted(numbers):", sorted(numbers))

# 20. slice → Extract part of a list
print("numbers[1:4]:", numbers[1:4])

print("="*50)
print("✅ All important list functions demonstrated!")


