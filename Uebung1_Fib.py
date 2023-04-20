import unittest

def fibonacci(x):
    try:
        n = int(x)
    except:
        raise ValueError("Wrong Input. Please enter an integer as argument")
    print("The first" , n, "Fibonacci numbers are:")
    for i in range (1, n):
        print(fib(i), ", ", sep = "", end="")
    print(fib(n))
    return fib(n)

def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib(n-1) + fib(n-2)

print("Please enter how many Fibonacci numbers you want to list:")
x = input()
fibonacci(x)

# Test

class TestFib(unittest.TestCase):
    def test_InputHandling(self):
        self.assertRaises(ValueError, fibonacci, "a"), "ValueError should occur"
    def test_Result(self):
        assert fib(6) == 8, "Result should be 8"
    
if __name__ == "__main__":
    unittest.main()
    

print("Please enter how many Fibonacci numbers you want to list:")
x = input()
fibonacci(x)


