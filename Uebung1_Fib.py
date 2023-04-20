
def Fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return Fib(n-1) + Fib(n-2)

print("Please enter how many Fibonacci numbers you want to list:")

n = int(input())

print("The first" , n, "Fibonacci numbers are:")

for i in range (1, n):
    print(Fib(i), ", ", sep = "", end="")
print(Fib(n))

