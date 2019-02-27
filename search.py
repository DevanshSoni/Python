import array as arr
print("How many values you wanna enter")
a=int(input())
b=list()
for i in range(0,a):
    b+=[int(input())]
c=arr.array('i',b)
print("Enter Value to search in array")
tar=int(input())
ch=0
for i in range(0,a):
    if c[i]==tar:
        print("Value found in the array")
        ch=1;
        break;
if ch==0:
    print("Value not found in the array")