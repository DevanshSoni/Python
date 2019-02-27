print("How many values you ant to enter into tuple ")
a=int(input())
b=()
for i in range(0,a):
    b+=(int(input()),)
for i in range(0,a):
    print(b[i])