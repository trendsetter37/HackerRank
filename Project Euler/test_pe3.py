import unittest
from pe3 import *

class TestGreatestPrimeFactor(unittest.TestCase):
	test_cases = [10, 17, 13195, 600851475143]
	test_case_answers = [5, 17, 29,6857]
	def test_prime_factorization(self):
		for idx, test in enumerate(self.test_cases):
			self.assertEqual(pfactorization(test), self.test_case_answers[idx])
if __name__ == '__main__':
	unittest.main()