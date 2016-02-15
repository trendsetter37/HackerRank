import unittest
from wetshark import wetshark as w

class WetSharkTestCase(unittest.TestCase):
    def setUp(self):
        self.testcases = (
        # of the form (cons, arr, answer)
            ('4 5 3', '1 1 1 4', 3),
            ('4 3 5', '1 1 1 4', 0),
            ('98 44 0', '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1', 810232479)

        )

    def test_dryshark(self):

        for test in self.testcases:
            cons = test[0]
            arr = test[1]
            self.assertEqual(test[2], w.dryshark(cons, arr))
'''
    def test_big_input(self):
        test = ('50 60 30', '1765 749 1244 1369 244 1998 1611 1734 864 1124 575 1125 1136 1716 1405 1880 1988 1715 175 573 1537 1953 301 434 216 38 1385 652 382 779 74 617 728 332 620 852 677 1228 1606 1033 416 1482 540 1113 390 1395 1093 1664 677 1111', 0)
        self.assertEqual(test[2], w.dryshark(test[0], test[1]))'''

if __name__ == '__main__':
    unittest.main()
