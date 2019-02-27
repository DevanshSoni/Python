import pandas as pd
res=pd.DataFrame({'x':[1,2,3,4,5],'y':[6,7,8,913,10]})
writer=ExcelWriter("hello.xlsx",engine="xlsxwriter")
res.toExcel(writer,sheet_name="Sheet1")
writer.save()
op=open("hello.xlsx","rb")
print(op)
