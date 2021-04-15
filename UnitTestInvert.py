import unittest
import InvertKeys

class Test(unittest.TestCase):
    def test_invert(self):
        self.assertEqual(InvertKeys.invert({"a": 1, "b": 2, "c": 3}), {1: "a", 2: "b", 3: "c"})

if __name__ == '__main__':
    unittest.main()