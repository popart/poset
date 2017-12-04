import unittest
from parse import create_matrix

class TestParse(unittest.TestCase):
    def test_create_matrix(self):
        expected = [[False, False, False, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False],
                    [False, False, False, False, False]]
        self.assertEqual(expected, create_matrix(5))

if __name__ == '__main__':
    unittest.main()
