import check_curly_braces
import unittest

class TestCurlyBraceCheckers(unittest.TestCase):
    
    examples_false = (("}", False), ("{", False), ("{}}", False))
    
    examples_true = (("", True), ("{}", True), ("{{}{}}", True))

    examples = examples_false + examples_true

    def test_stack_method_to_known_values(self):
        """Stack method should return the same boolean values as test cases"""
        for (s, expected_boolean) in self.examples:              
            actual_boolean = check_curly_braces.check_curlies_stack(s)                 
            self.assertEqual(expected_boolean, actual_boolean)   

    def test_counter_method_to_known_values(self):
        """Counter method should return the same boolean values as test cases"""
        for (s, expected_boolean) in self.examples:              
            actual_boolean = check_curly_braces.check_curlies_counter(s)
            self.assertEqual(expected_boolean, actual_boolean) 

if __name__ == '__main__':
    unittest.main()