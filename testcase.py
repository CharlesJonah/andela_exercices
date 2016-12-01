import unittest
from prime import prime_num

class TestKit(unittest.TestCase):
    
    #Checks to ensure that negative numbers are not used as parameters for the prime_num() function
    def test_negatives(self):
        self.assertEqual(prime_num(-10),"Only positive numbers are allowed")
    #Checks that if a certain number will return a list of prime numbers if it is supplied as an argument to the prime_num() function
    def test_output(self):
        self.assertEqual(prime_num(10), [2,3,5,7])
    
    #Checks that a string is not given a parameter to the prime_num() argument
    def test_string_input(self):
        self.assertEqual(prime_num("ten"),"Only numbers are allowed")
    
    #Checks that a float number is not given as a prime_num() argument 
    def test_float_input(self):
        self.assertEqual(prime_num(1.2),"Only integers to be used")
    
    #Checks that a very big number(upper boundary) is not supplied as a parameter to the prime_num() function
    def test_too_long_input(self):
        self.assertEqual(prime_num(999999999999),"Input is too long.")
    
    #Checks that one is not supplied as a parameter to the prime_num() function
    def test_one_as_input(self):
        self.assertEqual(prime_num(1),"One is not a prime number")
    
    #Checks that zero is not supplied as a parameter to the prime_num() function
    def test_zero_as_input(self):
        self.assertEqual(prime_num(0),"Zero is not a prime number")
    
    #Checks that prime_num() function is not supplied with an empty parameter
    def input_is_empty(self):
        self.assertEqual(prime_num(''),"You have not entered any number")
    
    #Checks that a dictionary is not used as a prime_num() function parameter
    def input_datatype_dict(self):
        self.assertEqual(prime_num({}),"Dictionary is not alllowed as an input")
        
    #Checks that a list is not as a prime_num() function parameter
    def input_datatype_list(self):
        self.assertEqual(prime_num([]),"List is not allowed as input")
