import binary_search
import unittest

class TestBinarySearch(unittest.TestCase):

    def test_method_to_built_in_method(self):
        """Method should return the same as 'in'""" 
        test_case_true = (1, [1,2,3])  # (needle, sorted_array)
        test_case_false = (4, [1,2,3])  # (needle, sorted_array)    
        self.assertEqual(test_case_true[0] in test_case_true[1], 
                        binary_search.binary_search(test_case_true[0], test_case_true[1]))   
if __name__ == '__main__':
    unittest.main()