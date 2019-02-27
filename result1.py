print("Enter Marks \n")
print("Enter Marks of Discrete mathematics\n")
a=int(input())
print("Enter Marks of Web Designing\n")
b=int(input())
print("Enter Marks of C++ \n")
c=int(input())
d=0
if a<40:
    if(d==0):
        print("You have supplementry in Discrete mathematics\n")
    d+=1
if b<40:
    if d==0:
        print("You have supplementry in Web designing \n")
    d+=1
if c<40:
    if d==0:
        print("You have supplementry in C++")
    d+=1
if(d>1):
    print("You Failed")
elif  d==0:
    print("You passed with the total of ",a+b+c," in all subjects")