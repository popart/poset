import unittest
from order import order

class TestOrder(unittest.TestCase):
    def test_order(self):
        test = [[False, False, False, False, False],
                [False, False, True, False, True],
                [True, False, False, False, True],
                [False, False, True, False, False],
                [True, False, False, False, False]]
        self.assertEqual(order(test), [0, 4, 2, 1, 3])

if __name__ == '__main__':
    unittest.main()
