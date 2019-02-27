print("how many numbers you wanna enter ",end="\n")
print("Numbers must be greater than 3",end="\n")
ab=int(input())
i=1
print("Enter Values ",end="\n")
a=b=c=int(input())
for i in range(ab):
  if i>0:
      n=int(input())
      if a<n:
          a,b,c=n,a,b
      elif b<n:
          b,c=n,b
      elif c<n:
          c=n

print("Highest is ",a,end="\n")
print("Second highest is ",b,end="\n")
print("Third Highest is ",c,end="\n")
