import unittest

# Iterative Ausfuehrung der Fibonacci Funktion

def fibonacci (x): 
    try: 
        n = int (x)
    except:
        raise ValueError("error - The method only accepts a number as parameter")
    if n < 1:
        raise ValueError("error - only values equal or greater than one are valid input values")
    prev = 0
    current = 1
    if n == 1:
        return 1
    for i in range (n-1):
        helper = current
        current += prev
        prev = helper
    return current

# Testteil

class Test_Fibonacci(unittest.TestCase):
    def test_InputHandling_NotANumber(self):
        self.assertRaises(ValueError, fibonacci, "a"), "ValueError should occur"
    def test_InputHandling_NumbersBelow1(self):
        self.assertRaises(ValueError, fibonacci, -1), "ValueError should occur"
    def test_InputHandling_Float(self):
        self.assertEqual(fibonacci(3.5), 2), "Result should be 2"
    def test_Result(self):
        self.assertEqual (fibonacci(6), 8), "Result should be 8"
    
if __name__ == "__main__":
    unittest.main()