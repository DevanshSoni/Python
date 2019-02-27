print("Enter Number to get series ")
a=int(input())
fib,fib1,fib3=0,1,0
print(fib)
print(fib1)
for i in range(2,a):
    fib3=fib+fib1
    print(fib3)
    fib,fib1=fib1,fib3
