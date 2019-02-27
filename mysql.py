import m
cursor=obj.cursor()
cursor.execute("select name from first;")
for i in cursor:
    print(i)