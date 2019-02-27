import array as arr
print("How many numbers you wanna enter into array ",end="\n")
a=int(input())
li=[]
for i in range(0,a):
    li+=[int(input())]
b=arr.array('i',li)
c=a-1
for i in range(0,int(a/2)):
    b[i],b[c]=b[c],b[i]
    c-=1
print("Reverse values of the array is ",end="\n")
for i in range(0,a):
    print(b[i],end="\n")