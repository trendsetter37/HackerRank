import unittest
from hr_collections import *


class TestCollection(unittest.TestCase):
    def setUp(self):
        self.X = 10
        self.sizes = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
        self.orders = (
            (6, 55),  # yes
            (6, 45),  # yes
            (6, 55),  # no
            (4, 40),  # yes
            (18, 60),  # yes
            (10, 50)  # no
        )
        self.counter_answer = 200

    def test_counter(self):
        self.assertEqual(profit(self.sizes, self.orders), self.counter_answer)

if __name__ == '__main__':
    unittest.main()
