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