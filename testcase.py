import unittest
from prime import prime_num
class TestKit(unittest.TestCase):
    def test_negatives(self):
        self.assertEqual(prime_num(-10),"Only positive numbers are allowed")

    def test_output(self):
        self.assertEqual(prime_num(10), [2,3,5,7])

    def test_string_input(self):
        self.assertEqual(prime_num("ten"),"Only numbers are allowed")

    def test_float_input(self):
        self.assertEqual(prime_num(1.2),"Only integers to be used")

    def test_too_long_input(self):
        self.assertEqual(prime_num(999999999999),"Input is too long.")

    def test_one_as_input(self):
        self.assertEqual(prime_num(1),"One is not a prime number")

    def test_zero_as_input(self):
        self.assertEqual(prime_num(0),"Zero is not a prime number")

    def input_is_empty(self):
        self.assertEqual(prime_num(''),"You have not entered any number")

    def input_datatype_dict(self):
        self.assertEqual(prime_num({}),"Dictionary is not alllowed as an input")

    def input_datatype_list(self):
        self.assertEqual(prime_num([]),"List is not allowed as input")