print("Enter How many values you wanna enter \n")
i,a=1,int(input())
print("Enter Values ")
b=int(input())
m=b
s=0
for i in range(a):
    b=int(input())
    if b>m:
        s,m=m,b
    elif s<b:
        s=b
print("Second highest in the entered numbers is ",s)