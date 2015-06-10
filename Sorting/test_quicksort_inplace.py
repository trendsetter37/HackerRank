from __future__ import print_function

import unittest
from quicksort_inplace import *

class TestQuicksort(unittest.TestCase):

	def setUp(self):
		x = [3,4,1, 5,2]
		x_answer = [i for i in range(1,6)]

		y = [-3,2,-5,4,1,-1, 5,-2,-4,3,0]
		y_answer = [i for i in range(-5, 6)]
		self.test_case = [x,y]
		self.test_case_answers = [x_answer, y_answer]

	def test_quicksort(self):

		for idx, test in enumerate(self.test_case):
			
			print("Test is: {}".format(test))
			quicksort(test, 0, len(test)-1)
			print("Result is: {}".format(test))
			self.assertEqual(test, self.test_case_answers[idx])
			
if __name__ == '__main__':
	unittest.main()