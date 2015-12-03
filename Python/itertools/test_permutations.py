import unittest
from permutations import permute, combinate


class TestPermutations(unittest.TestCase):
    def setUp(self):
        self.sample_input = 'HACK 2'
        self.sample_output = 'AC\nAH\nAK\nCA\nCH\nCK\nHA\n' + \
            'HC\nHK\nKA\nKC\nKH'
        self.sample_output_combin = 'A\nC\nH\nK\nAC\nAH\nAK\nCH\nCK\nHK'

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

if __name__ == '__main__':
    unittest.main()
