import fizzbuzz
import unittest

class TestFizzBuzz(unittest.TestCase):
    
    test_cases_fizz = [(3,'Fizz'), (6, 'Fizz')]
    test_cases_buzz = [(5,'Buzz'), (10, 'Buzz')]
    test_cases_fizzbuzz = [(15,'FizzBuzz'), (30, 'FizzBuzz')]
    test_cases_strings = test_cases_fizz + test_cases_buzz + test_cases_fizzbuzz

    test_case_numbers = [(1,1), (2,2), (98,98)]

    def test_method_to_strings(self):
        """Test numbers are replaced with proper strings"""
        for (n, expected_result) in self.test_cases_strings:              
            actual_result = fizzbuzz.fizzbuzz(n)       
            self.assertEqual(expected_result, 
                            actual_result,
                            "Current method failed for the number: {}".format(n))   
    
    def test_method_to_numbers(self):
        for (n, expected_result) in self.test_case_numbers:  
            actual_result = fizzbuzz.fizzbuzz(n)
            self.assertEqual(expected_result, 
                            actual_result,
                            "Current method failed for the number: {}".format(n))  

if __name__ == '__main__':
    unittest.main()