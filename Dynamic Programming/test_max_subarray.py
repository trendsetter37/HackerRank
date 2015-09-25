import sys
import os
import json
import unittest
from maximum_subarray import dp

class TestCase2(unittest.TestCase):
	def setUp(self):
		self.test_arrays = []
		self.outputs = []

		if os.path.isfile('inputs.json'):
			with open('inputs.json', 'r') as inputs:
				self.test_arrays = json.load(inputs)
			print 'Testcases: {}'.format(len(self.test_arrays))
		else:
			f = open('testcase2.txt', 'r')
			self.test_cases = int(f.readline())
			# pull in inputs
			for i in xrange(self.test_cases):
				_ = f.readline()
				self.test_arrays.append(map(int, f.readline().split()))
			with open('inputs.json', 'w') as outfile:
				json.dump(self.test_arrays, outfile)
			print 'Testcases: {}'.format(self.test_cases)
			f.close()

		if os.path.isfile('outputs.json'):
			with open('outputs.json', 'r') as outputs:
				self.outputs = json.load(outputs)
			print self.outputs
		else:
			f1 = open('testcase2_output.txt', 'r')
			self.outputs = [a.split() for a in f1.read().split('\r\n')]	
			with open('outputs.json', 'w') as outfile:
				json.dump(self.outputs, outfile)
			f1.close()
			print self.outputs		


	def teardown(self):
		self.test_arrays.dispose()
		self.outputs.dispose()
		self.test_arrays = None
		self.outputs = None

	def test_answers_against_test_case2_outputs(self):

		for idx, test in enumerate(self.test_arrays):
			print 'Test: {}'.format(idx + 1)
			result = dp(test)
			self.assertEqual(result, self.outputs[idx])

if __name__ == '__main__':
	unittest.main()


		