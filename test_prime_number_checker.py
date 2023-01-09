import prime_number_checker
import unittest

class TestPrimeChecker(unittest.TestCase):
    
    test_cases_special = [(1, False)]
    test_cases_false = [(4, False), (33, False)]
    test_cases_true = [(2, True), (3, True), (5, True), (31, True)]
    test_cases = test_cases_false + test_cases_true + test_cases_special

    def test_method_to_known_values(self):
        """Method should return the same boolean values as test cases"""
        for (n, expected_boolean) in self.test_cases:              
            actual_boolean = prime_number_checker.is_prime(n)       
            self.assertEqual(expected_boolean, 
                            actual_boolean,
                            "Current method failed for the number: {}".format(n))   

if __name__ == '__main__':
    unittest.main()