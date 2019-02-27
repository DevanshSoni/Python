print("Enter Number to find whether it's prime or not",end='\n')
a=int(input())
b=1
for i in range(int(a/2)+1):
    print("Hello")
    if i>1:
      if int(a%i)==0 :
        b=0
        break

if b==0:
    print("It's not a prime number ",end='\n')
elif b==1:
    print("Number is prime",end='\n')