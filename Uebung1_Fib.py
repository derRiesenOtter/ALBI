import unittest

# Aufrufende Funktion (nicht sonderlich effektiv, da die Werte alle einzeln berechnet werden. Iterativ waere besser gewesen.)

def fibonacci(x):
    try:
        n = int(x)
        if n <= 0:
            raise ValueError("Wrong Input. Please enter an integer greater than 0.")
        print("The first" , n, "Fibonacci numbers are:")
        for i in range (1, n):
            print(fib(i), ", ", sep = "", end="")
        print(fib(n))
        return fib(n)    
    except:
        raise ValueError("Wrong Input. Please enter an integer as argument.")
    

# eigentliche berechnende Funktion

def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib(n-1) + fib(n-2)

# Komplexität rekursiv ist schlecht: O(n^2) - iterativ ist besser O(n).

# Aufruf wie folgt (wegen unittest außerhalb der eigentlichen Funktion):
print("Please enter how many Fibonacci numbers you want to list:")
x = input()
fibonacci(x)

# Test

class TestFibonacci(unittest.TestCase):
    def test_InputHandling(self):
        self.assertRaises(ValueError, fibonacci, "a"), "ValueError should occur"
    def test_Result(self):
        self.assertEqual (fibonacci(6), 8), "Result should be 8"
    
if __name__ == "__main__":
    unittest.main()
    

