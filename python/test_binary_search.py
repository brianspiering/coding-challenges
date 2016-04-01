import binary_search
import unittest

class TestBinarySearch(unittest.TestCase):

    test_cases_true = [(3, [1,2,3,4,5])]  # (needle, sorted_array)
    test_cases_false = [(4, [1,2,3])] # (needle, sorted_array)    
    test_cases = test_cases_true + test_cases_false

    def test_method_to_built_in_method(self):
        """Method should return the same as 'in'""" 
        for (needle, sorted_array) in self.test_cases:                              
            self.assertEqual(needle in sorted_array,
                             binary_search.binary_search(needle, sorted_array))    

if __name__ == '__main__':
    unittest.main()