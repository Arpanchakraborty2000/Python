import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Arpan", "Riya", "Sam", "John", "Tina"],
    "Age": [25, 30, 18, 40, 22],
    "City": ["Kolkata", "Delhi", "Mumbai", "Delhi", "Pune"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 🔹 1. Select rows where Age > 25
print("\nPeople older than 25:")
print(df[df["Age"] > 25])

# 🔹 2. Select rows where City == 'Delhi'
print("\nPeople from Delhi:")
print(df[df["City"] == "Delhi"])

# 🔹 3. Multiple conditions (Age > 20 AND City == 'Pune')
print("\nPeople older than 20 and from Pune:")
print(df[(df["Age"] > 20) & (df["City"] == "Pune")])

# 🔹 4. OR condition (Age < 20 OR City == 'Kolkata')
print("\nPeople younger than 20 OR from Kolkata:")
print(df[(df["Age"] < 20) | (df["City"] == "Kolkata")])
