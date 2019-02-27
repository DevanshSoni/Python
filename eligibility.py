print("Enter Marks to check eligibility\n")
a=int(input("Enter Marks of Maths \n"))
b=int(input("Enter Marks of Physics \n"))
c=int(input("Enter Marks of Chemistry \n"))
d=a+b+c;
if a>=55 and b>=55 and c>=50 and (d>=180 or a+b>=140):
    print("You're eligible for admission");