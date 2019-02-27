print("Enter How many numbers you wanna enter into list")
a=int(input())
print("Enter Values ",end="\n")
b=[]
for i in range(a):
    n=int(input())
    b+=[n]
i=0
count=0
ch=1
for i in range(a):
    for j in range(int(b[i]/2)+1):
       ch=1
       if j>1:
        if b[i]%j==0:
           ch=0
           break
    if ch==1:
          count+=1
print("Number of prime numbers in the list are ",count)