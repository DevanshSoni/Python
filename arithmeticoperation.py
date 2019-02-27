print("Enter Two Numbers to perform operations")
a=int(input("Enter First Number \n"))
b=int(input("Enter Second Number \n"))
print("Select operation to be performed \n")
print("1 for Addition \n")
print("2 for Multiplication \n")
print("3 for Division \n")
print("4 for Modulus \n")
print("5 for subtraction \n")
c=int(input())
if c==1:
    print(a+b)
if c==2:
    print(a*b)
if c==3:
    print(a/b)
if c==4:
    print(a%b)
if c==5:
    if a>b:
        print (a-b)
    if b>a:
        print(b-a)
    if a==b:
        print(0);