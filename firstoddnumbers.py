print("Enter how many numbers you wanna enter")
a=int(input())
i=1
b=[]
sum=0
while i<=a:
    b+=[int(input())]
    i+=1
for i in range(0,a):
    if b[i]%2!=0:
       sum+=b[i]
print("Sum of odd numbers in the list is ",sum)