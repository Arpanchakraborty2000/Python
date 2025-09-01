import pandas as pd
import numpy as np

# Create a DataFrame with some null values
data = {
    "Name": ["Arpan", "Riya", "Sam", None, "John"],
    "Age": [25, None, 30, 28, None],
    "City": ["Kolkata", "Delhi", None, "Mumbai", "Pune"]
}

df = pd.DataFrame(data)

print("DataFrame with Null Values:")
print(df)

# Check for null values
print("\nCheck Null Values:")
print(df.isnull())
