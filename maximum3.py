print("Enter three numbers to find out the maximum")
a=int(input("Enter First number\n"))
b=int(input("Enter second number\n"))
c=int(input("Enter third number\n"))
if a>b:
    if a>c or a==c:
      print(a," is greater among all")
if b>a:
    if b>c or b==c:
      print(b," is greater among all")
if c>a:
    if c>b or c==b:
      print(c," is greater among all")
if a>c and a==b:
    print(a," is greater among all ")
if a==b and a==c:
    print("All numbers are equal")