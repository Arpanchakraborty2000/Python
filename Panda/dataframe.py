import pandas as pd
import numpy as np

print(np.arange(0,20).reshape(5,4)) # 5 rows and 4 colums 
print("#################################")
df=pd.DataFrame(data=np.arange(0,20).reshape(5,4),index=["row1","row2","row3","row4","row5"],columns=["col1","col2","col3","col4"])
print("Print dataframe: \n", df)
print("#################################")
print("Fast five row : \n",df.head())

print("#################################")
print("Last five row : \n",df.tail()) # () <- in this braces if you mantion the number the it show that was ........

print("#################################")
print("This will print info of column : \n",df.info()) # print information of column 

print("#################################")
print("This will print describe  of column : \n",df.describe())

print("#################################")
print(df['col1'])  # If you provide how much column it will print this much .....
print(type(df['col1']) )

print("#################################")
print(df[['col1','col2','col3']]) # It will print 3 col .....

## By Using Row index name using loc  --------------
print("#################################")
print(df.loc[['row3','row4']])


### Searching with row index and column index number 

print("#################################")
print(df.head())
print("#################################")
print(df.iloc[2:4,0:2])


## Convert dataframe to array
print("#################################")
print("Convert dataframe to array ")
print(df.iloc[2:4,0:2].values)