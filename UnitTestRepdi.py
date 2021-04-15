import unittest
import Repdigit

class Test(unittest.TestCase):
    def test_repdigit(self):
        self.assertEqual(Repdigit.repdigit(6), True)
        self.assertEqual(Repdigit.repdigit(66), True)
        self.assertEqual(Repdigit.repdigit(666), True)
        self.assertEqual(Repdigit.repdigit(6666), True)
        self.assertEqual(Repdigit.repdigit(1001), False)
        self.assertEqual(Repdigit.repdigit(-11), False, "The number must be >= 0")

if __name__ == '__main__':
    unittest.main()