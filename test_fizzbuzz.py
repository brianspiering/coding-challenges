import fizzbuzz
import unittest

class TestFizzBuzz(unittest.TestCase):
    
    test_cases_fizz = [(3,'Fizz'), (6, 'Fizz')]
    test_cases_buzz = [(5,'Buzz'), (10, 'Buzz')]
    test_cases_fizzbuzz = [(15,'FizzBuzz'), (30, 'FizzBuzz')]
    test_cases = test_cases_fizz + test_cases_buzz + test_cases_fizzbuzz

    def test_method_to_strings(self):
        """"""
        for (n, expected_result) in self.test_cases:              
            actual_result = fizzbuzz.fizzbuzz(n)       
            self.assertEqual(expected_result, 
                            actual_result,
                            "Current method failed for the number: {}".format(n))   
    
    def test_method_to_numbers(self):
        pass

if __name__ == '__main__':
    unittest.main()