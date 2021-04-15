import unittest
import ListMultiplier

class Test(unittest.TestCase):
    def test_list(self):
        self.assertEqual(ListMultiplier.multiply(["/", "*", "+"]), [["/", "/", "/"], ["*", "*", "*"], ["+", "+", "+"]])

if __name__ == '__main__':
    unittest.main()