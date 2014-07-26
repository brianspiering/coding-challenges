import check_curly_braces
import unittest

class TestCurlyBraceCheckers(unittest.TestCase):
    
    examples_false = (("}", False), ("{", False), ("{}}", False))
    
    examples_true = (("", True), ("{}", True), ("{{}{}}", True))

    examples = examples_false + examples_true

    def test_stack_method_to_known_values(self):
        """Stack method should give known result with known input"""
        for (s, boolean) in self.examples:              
            result = check_curly_braces.check_curlies_stack(s)                 
            self.assertEqual(boolean, result)   

    def test_counter_method_to_known_values(self):
        """Counter method should give known result with known input"""
        for (s, boolean) in self.examples:              
            result = check_curly_braces.check_curlies_counter(s)
            self.assertEqual(boolean, result) 

if __name__ == '__main__':
    unittest.main()