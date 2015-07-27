import unittest
from pe2 import *

class ProjectEuler2Test(unittest.TestCase):
	

	def test_fibsum_answers(self):
		self.test_cases = (10, 100, 4*10**6) # that last one will test 4 million
		self.answers = (10, 44, 4613732, )
		for idx, tc in enumerate(self.test_cases):
			self.assertEqual(fibsum(tc), self.answers[idx])


if __name__ == '__main__':
	unittest.main()