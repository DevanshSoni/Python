print("Enter how many numbers you wanna enter")
a=int(input())
print("Enter Values ",end="\n")
b=list()
count=0
m=0
for i in range(a):
    ch=1
    b+=[int(input())]
    for j in range(int(b[i]/2)+1):
        if j>1:
            if b[i]%j==0:
                ch=0
                break
    if ch==1:
       if m<b[i]:
           m=b[i]
       count+=1
print("There is ",count," prime numbers in the list",end="\n")
print("Highest prime number in the list is ",m,end="\n")