import unittest
import SumofMissingNumbers

class Test (unittest.TestCase):
    def test_sumof(self):
        self.assertEqual(SumofMissingNumbers.sum_missing_numbers([4, 3, 8, 1, 2]), 18)
        

if __name__ == '__main__':
    unittest.main()