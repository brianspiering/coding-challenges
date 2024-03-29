from fizzbuzz  import fizz_buzz
import unittest

class TestFizzBuzz(unittest.TestCase):
    
    test_cases_fizz = [(3,'Fizz'), (6, 'Fizz')]
    test_cases_buzz = [(5,'Buzz'), (10, 'Buzz')]
    test_cases_fizzbuzz = [(15,'FizzBuzz'), (30, 'FizzBuzz')]
    test_cases_strings = test_cases_fizz + test_cases_buzz + test_cases_fizzbuzz

    test_case_numbers = [1, 2, 4, 16]

    def test_method_with_strings(self):
        """Test numbers are replaced with proper strings"""
        for (n, expected_result) in self.test_cases_strings:              
            actual_result = fizz_buzz(n)       
            self.assertEqual(expected_result, 
                            actual_result,
                            f"Current method failed for the number: {n}")   
    
    def test_method_with_numbers(self):
        for n in self.test_case_numbers:  
            actual_result = fizz_buzz(n)
            expect_restult = str(n)
            self.assertEqual(expect_restult, 
                            actual_result,
                            f"Current method failed for the number: {n}")  

if __name__ == '__main__':
    unittest.main()