import sys
import os
import json
import unittest
import time
from maximum_subarray import dp

class TestCase2(unittest.TestCase):
	def setUp(self):
		self.test_arrays = []
		self.outputs = []

		if os.path.isfile('inputs/inputs.json'):
			with open('inputs/inputs.json', 'r') as inputs:
				self.test_arrays = json.load(inputs)
			#print 'Testcases: {}'.format(len(self.test_arrays))
		else:
			f = open('text_files/testcase2.txt', 'r')
			self.test_cases = int(f.readline())
			# pull in inputs
			for i in xrange(self.test_cases):
				_ = f.readline()
				self.test_arrays.append(map(int, f.readline().split()))
			with open('inputs/inputs.json', 'w') as outfile:
				json.dump(self.test_arrays, outfile)
			#print 'Testcases: {}'.format(self.test_cases)
			f.close()

		if os.path.isfile('outputs/outputs.json'):
			with open('outputs/outputs.json', 'r') as outputs:
				self.outputs = json.load(outputs)
			#print self.outputs
		else:
			f1 = open('text_files/testcase2_output.txt', 'r')
			self.outputs = [a.split() for a in f1.read().split('\r\n')]	
			with open('outputs/outputs.json', 'w') as outfile:
				json.dump(self.outputs, outfile)
			f1.close()
			#print self.outputs		


	def teardown(self):
		self.test_arrays.dispose()
		self.outputs.dispose()
		self.test_arrays = None
		self.outputs = None

	def test_answers_against_test_case2_outputs(self):

		for idx, test in enumerate(self.test_arrays):
			
			result = dp(test)
			self.assertEqual(result, self.outputs[idx])

class TestCase1(unittest.TestCase):

	def setUp(self):
		self.test_arrays = []
		self.outputs = []

		if os.path.isfile('inputs/inputs1.json'):
			with open('inputs/inputs1.json', 'r') as inputs:
				self.test_arrays = json.load(inputs)
			#print 'Testcases: {}'.format(len(self.test_arrays))
		else:
			f = open('text_files/testcase1.txt', 'r')
			self.test_cases = int(f.readline())
			# pull in inputs
			for i in xrange(self.test_cases):
				_ = f.readline()
				self.test_arrays.append(map(int, f.readline().split()))
			with open('inputs/inputs1.json', 'w') as outfile:
				json.dump(self.test_arrays, outfile)
			#print 'Testcases: {}'.format(self.test_cases)
			f.close()

		if os.path.isfile('outputs/outputs1.json'):
			with open('outputs/outputs1.json', 'r') as outputs:
				self.outputs = json.load(outputs)
			#print self.outputs
		else:
			f1 = open('text_files/testcase1_output.txt', 'r')
			self.outputs = [a.split() for a in f1.read().split('\r\n')]	
			with open('outputs/outputs1.json', 'w') as outfile:
				json.dump(self.outputs, outfile)
			f1.close()
			#print self.outputs		

	def teardown(self):
		self.test_arrays.dispose()
		self.outputs.dispose()
		self.test_arrays = None
		self.outputs = None

	def test_answers_against_test_case1_outputs(self):

		for idx, test in enumerate(self.test_arrays):
			
			result = dp(test)
			self.assertEqual(result, self.outputs[idx])

class TestCase3(unittest.TestCase):
	def setUp(self):
		self.test_arrays = []
		self.outputs = []

		if os.path.isfile('inputs/inputs3.json'):
			with open('inputs/inputs3.json', 'r') as inputs:
				self.test_arrays = json.load(inputs)
			#print 'Testcases: {}'.format(len(self.test_arrays))
		else:
			f = open('text_files/testcase3.txt', 'r')
			self.test_cases = int(f.readline())
			# pull in inputs
			for i in xrange(self.test_cases):
				_ = f.readline()
				self.test_arrays.append(map(int, f.readline().split()))
			with open('inputs/inputs3.json', 'w') as outfile:
				json.dump(self.test_arrays, outfile)
			#print 'Testcases: {}'.format(self.test_cases)
			f.close()

		if os.path.isfile('outputs/outputs3.json'):
			with open('outputs/outputs3.json', 'r') as outputs:
				self.outputs = json.load(outputs)
			#print self.outputs
		else:
			f1 = open('text_files/testcase3_output.txt', 'r')
			self.outputs = [a.split() for a in f1.read().split('\r\n')]	
			with open('outputs/outputs3.json', 'w') as outfile:
				json.dump(self.outputs, outfile)
			f1.close()
			#print self.outputs		

	def teardown(self):
		self.test_arrays.dispose()
		self.outputs.dispose()
		self.test_arrays = None
		self.outputs = None

	def test_answers_against_test_case3_outputs(self):

		for idx, test in enumerate(self.test_arrays):
			
			result = dp(test)
			self.assertEqual(result, self.outputs[idx])

class TestCase4(unittest.TestCase):
	def setUp(self):
		self.test_arrays = []
		self.outputs = []

		if os.path.isfile('inputs/inputs4.json'):
			with open('inputs/inputs4.json', 'r') as inputs:
				self.test_arrays = json.load(inputs)
			#print 'Testcases: {}'.format(len(self.test_arrays))
		else:
			f = open('text_files/testcase4.txt', 'r')
			self.test_cases = int(f.readline())
			# pull in inputs
			for i in xrange(self.test_cases):
				_ = f.readline()
				self.test_arrays.append(map(int, f.readline().split()))
			with open('inputs/inputs4.json', 'w') as outfile:
				json.dump(self.test_arrays, outfile)
			#print 'Testcases: {}'.format(self.test_cases)
			f.close()

		if os.path.isfile('outputs/outputs4.json'):
			with open('outputs/outputs4.json', 'r') as outputs:
				self.outputs = json.load(outputs)
			#print self.outputs
		else:
			f1 = open('text_files/testcase4_output.txt', 'r')
			self.outputs = [a.split() for a in f1.read().split('\r\n')]	
			with open('outputs/outputs4.json', 'w') as outfile:
				json.dump(self.outputs, outfile)
			f1.close()
			#print self.outputs		

	def teardown(self):
		self.test_arrays.dispose()
		self.outputs.dispose()
		self.test_arrays = None
		self.outputs = None

	def test_answers_against_test_case4_outputs(self):

		for idx, test in enumerate(self.test_arrays):
			
			result = dp(test)
			self.assertEqual(result, self.outputs[idx])

if __name__ == '__main__':
	logfile = 'logs/test_log_file.txt'
	f = open(logfile, 'w')
	runner = unittest.TextTestRunner(f)
	the_time = '* ' + time.asctime(time.localtime()) + ' *\n' 
	tl = len(the_time)
	borders = ('*' * (tl-1)) + '\n' # top and bottom borders
	f.write(borders + the_time + borders)
	unittest.main(testRunner=runner)
	f.close()
	

	





		