import sleep_in
import unittest

class TestSleepIn(unittest.TestCase):
    
    # [(input_1, input_2), answer]
    test_cases= [((False, False), True),
                ((True, False), False),
                ((False, True), True),
                ((True, True), True)]

    def test_method_(self):
        """Test methods returns expected boolean"""
        for (boolean_pair, expected_result) in self.test_cases:              
            actual_result = sleep_in.sleep_in(boolean_pair[0], boolean_pair[1])       
            self.assertEqual(expected_result, 
                            actual_result,
                            "Current method failed for the boolean pair: {}".format(boolean_pair))   

if __name__ == '__main__':
    unittest.main()