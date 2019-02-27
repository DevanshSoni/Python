import array as arr
import operator
print("How many values you wanna enter into array")
a=int(input())
b=list()
print("Enter values ",end="\n")
for i in range(0,a):
      b+=[int(input())]
c=arr.array('i',b)
for i in range(0,a-1):
    for j in range(i+1,a-1):
        if c[i]==c[j]:#c[i]==c[j
            c.remove(c[j])
            a-=1;
#my =c.len()
for i in range (0,a):
    print(c[i])