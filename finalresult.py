a=int(input("Enter Roll No"))
b=input("Enter your Name")
m=int(input("Enter marks in Mathematics\n"))
p=int(input("Enter Marks in Physics \n"))
c=int(input("Enter Marks in Chemistry \n"))
d=m+p+c
temp=check=0
res=""
per=float(d/3)
if m<40:
    if m+3>=40:
     check=1
    temp+=1
elif p<40:
    if temp==0:
        if p+3>=40:
            check=1
    temp+=1
elif c<40:
    if temp==0:
        if c+3>=40:
            check=1
    temp+=1
if temp==0:
    res="Pass"
elif temp==1 and check==1:
    res="Pass with grace"
elif temp==1:
    res="Supplementry "
elif temp>1:
    res="Fail"
print("\t\t\tMaharishi Arvind Institute of Science and Management\n")
print("\t Roll No :- ",a,"\t Name :-",b,end ="\n")
print("\t_____________________________________________________________\n")
print("Subject\tMax Marks\tMin Marks\tMarksobt\n")
print("\tMaths\t100\t40\t",m,end="\n")
print("\tPhys.\t100\t40\t",p,end="\n")
print("\tChem.\t100\t40\t",c,end="\n")
print("\tTotal :- ",d,"\t Percentage :-",per,end="\n")
print("\tResult:-",res,end="\n")
print("\t_____________________________________________________________\n")