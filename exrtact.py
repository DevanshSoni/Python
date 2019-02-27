import pandas as pd
import numpy as np
fetch=open("pandas.xlsx","rb")
read=pd.read_excel(fetch)
con=read[['a','b']]
con=np.array(con)
print(con[0:2,1])