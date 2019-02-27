import array as arr
print("How many numbers you wanna enter into array")
a=int(input())
print("Enter Values ",end="\n")
b=[]
for i in range(0,a):
    b+=[int(input())]
array1=arr.array('i',b)
temp=array1[0]
for i in range(0,a-1):
    array1[i]=array1[i+1]
array1[a-1]=temp
for i in range(0,a):
    print(array1[i],end="\n")