import unittest
from permutations import permute, combinate, combinate_with_replace, Acount


class TestPermutations(unittest.TestCase):
    def setUp(self):
        self.sample_input = 'HACK 2'
        self.sample_output = 'AC\nAH\nAK\nCA\nCH\nCK\nHA\n' + \
            'HC\nHK\nKA\nKC\nKH'
        self.sample_output_combin = 'A\nC\nH\nK\nAC\nAH\nAK\nCH\nCK\nHK'
        self.replacement_output = 'AA\nAC\nAH\nAK\nCC\nCH\nCK\nHH\nHK\nKK'

    def test_permute_function(self):
        self.assertEqual(
            permute(self.sample_input),
            self.sample_output
        )

    def test_combinate_function(self):
        self.assertEqual(
            combinate(self.sample_input),
            self.sample_output_combin
        )

    def test_combinate_with_replacement(self):
        self.assertEqual(
            combinate_with_replace(self.sample_input),
            self.replacement_output
        )


class TestProbabilityClass(unittest.TestCase):
    def setUp(self):
        self.test_case = 'a a b c'
        self.l = self.test_case.split()
        self.k = 2
        self.answer = 0.8333333
        self.a_count = Acount(self.l, self.k)

    def test_prob_class(self):
        self.assertAlmostEqual(self.a_count.prob, self.answer, places=3)

if __name__ == '__main__':
    unittest.main()
