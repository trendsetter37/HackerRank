import unittest
from filling_jars import *
# to run this unittest.main()
# Not working as of now
class TestCases(unittest.TestCase):
	t1 = []
	ta = []
	result = []

	def setUp(self):
		# Pull in TestCases
		testcase1 = open('testcase6.txt', 'r')
		t1 = testcase1.readlines()

		testcase_answer = open('testcase6_output.txt', 'r')

		self.ta = testcase_answer.readlines()
		N_M = t1[0]
		N = N_M.split()[0]
		M = N_M.split()[1]
		self.result = [0] * int(N)
		



	def test_against_answers(self):
		
		for thing in self.t1:
			self.result = operation(*thing.split())
		self.assertEqual(avg(self.result), int(self.ta[0]))

	def teardown(self):
		t1.close()
		ta.close()



