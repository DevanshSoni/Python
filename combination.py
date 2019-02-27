print("Enter Values of n")
a=int(input())
print("Enter Value of r")
b=int(input())
f=r=j=1
for i in range(1,a+1):
    f=f*i
for i in range(1,b+1):
    r=r*i
for i in range(1,(a-b)+1):
    j=j*i
b=float(f/(r*j))
print("Number of Combinations is ",b)