import array as arr
print("How many values you wanna enter ",end="\n")
a=int(input())
b=[]
for i in range(0,a):
    b+=[int(input())]
c=arr.array('i',b)
temp=c[a-1]
i=a-1
while (i!=0):
         c[i]=c[i-1]
         i-=1
c[0]=temp
for i in range(0,a):
    print(c[i],end="\n")
