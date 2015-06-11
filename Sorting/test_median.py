
import unittest
import statistics # only in python 3.4
import random
import median

class TestMedian(unittest.TestCase):
	y_answer = 0
	x_answer = 0

	def setUp(self):
		x = [2,4,1,3,7]
		self.x_answer = 3

		y = [random.randint(1,100) for i in range(100)]
		y_anwer = statistics.median(y)
		self.tests = [x,y]
		self.test_answers = [self.x_answer, self.y_answer]		

	def test_median(self):
		for idx, test in enumerate(self.tests):
			my_result = median.median(test, 0, len(test)-1)
			statistics_result = self.test_answers[idx]
			self.assertEqual(my_result, statistics_result)

if __name__ == '__main__':
	unittest.main()