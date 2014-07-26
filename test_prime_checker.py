import prime_number_checker
import unittest

class TestPrimeChecker(unittest.TestCase):
    
    examples_false = ((1, False), (4, False), (33, False))
    
    examples_true = ((2, True), (3, True), (5, True), (31, True))

    examples = examples_false + examples_true

    def test_method_to_known_values(self):
        """Method should return the same boolean values as test cases"""
        for (n, expected_boolean) in self.examples:              
            actual_boolean = prime_number_checker.is_prime(n)                 
            self.assertEqual(expected_boolean, actual_boolean)   

if __name__ == '__main__':
    unittest.main()