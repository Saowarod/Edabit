import unittest
import Concatenate

class Test(unittest.TestCase):
    def test_concat(self):
        self.assertEqual(Concatenate.concat([1, 2, 3], [4, 5], [6, 7]), [1, 2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()