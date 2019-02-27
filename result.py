print("Enter Marks of subjects")
a=int(input())
b=int(input())
c=int(input())
d=a+b+c;
e=float(d/3)
if e>=80:
    print("Total is ",d,"\n Percentage obtained ",e,"\n having First Division ")
elif e>=70 and e<80:
    print("Total is ",d,"\n Percentage Obtained ",e,"\n having Second Division ")
elif e<70:
    print("Total is ",d,"\n Percentage Obtained ",e,"\n having Third Division ")