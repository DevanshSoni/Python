a=input("Enter your Name")
b=input("Enter your ID")
c=float(input("Enter Unit Consumed"))
d=0.0
if c<=199:
    d=c*1.20
elif c>=200 and c<400:
    d=(199*1.20)+(c-199)*1.50
elif c>=400 and c<600:
    d=(199*1.20)+(200*1.50)+(c-399)*1.80
elif c>=600:
    d=(199*1.20)+(200*1.50)+(200*1.80)+(c-599)*2.00
if d>400:
    d=d+d*(15/100)
if(d<200):
    d=200
print("Customer ID is " ,b,end="\n")
print("Customer Name is ",a,end="\n")
print("Total Unit Consumed is ",c,end="\n")
print("Total Bill to be paid is ",d,end="\n")