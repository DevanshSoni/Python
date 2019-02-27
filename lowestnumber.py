print("Enter how many numbers you wanna enter")
ab=int(input())
print("Enter Values",end="\n")
a=list()
for i in range(0,ab):
    n=int(input())
    a+=[n]
b=min(a)
print(b)