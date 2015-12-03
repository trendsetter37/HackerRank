import unittest
from permutations import permute


class TestPermutations(unittest.TestCase):
    def setUp(self):
        self.sample_input = 'HACK 2'
        self.sample_output = 'AC\nAH\nAK\nCA\nCH\nCK\nHA\n' + \
            'HC\nHK\nKA\nKC\nKH'

    def test_permute_function(self):
        self.assertEqual(
            permute(self.sample_input),
            self.sample_output
        )

if __name__ == '__main__':
    unittest.main()
