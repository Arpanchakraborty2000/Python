from io import StringIO
import pandas as pd 

df= pd.read_excel('Untitled.xlsx')

print(df.head())
print(type(df))