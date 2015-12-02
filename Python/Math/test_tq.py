import unittest
from triangle_quest import repunit, demlo_numbers


class TestRepUnit(unittest.TestCase):

    def setUp(self):
        self.tests = (1, 2, 3, 4, 5)
        self.repunit_answers = (1, 11, 111, 1111, 11111)
        self.demlo_answers = (1, 121, 12321, 1234321, 123454321)

    def test_repunit(self):
        for i in xrange(1, 6):
            self.assertEqual(repunit(i), self.repunit_answers[i - 1])

    def test_demlo(self):
        for i in xrange(1, 6):
            self.assertEqual(demlo_numbers(
                repunit(i)), self.demlo_answers[i - 1]
                )

if __name__ == '__main__':
    unittest.main()
