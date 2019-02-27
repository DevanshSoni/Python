import array as arr
print("Enter How many values you wanna enter into array")
a=int(input())
b=list()
for i in range(a):
    b+=[int(input())]
c=arr.array('i',b)
for i in range(0,a):
    for j in range(i+1,a):
       if c[i]>c[j]:
         temp=c[i]
         c[i]=c[j]
         c[j]=temp

for i in range(0,a):
    print(c[i])