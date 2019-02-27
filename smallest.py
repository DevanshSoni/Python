print("Enter four numbers to get the smallest number\n")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if b>a and c>a and d>a:
    print(a, " is the smallest number")
elif a>b and c>b and d>b:
    print(b," is the smallest among all")
elif a>c and b>c and d>c:
    print(c," is the smallest among all")
elif a>d and b>d and c>d:
    print(d," is the smallest among all")