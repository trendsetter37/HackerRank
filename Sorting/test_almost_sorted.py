import unittest
import random
import sys
from almost_sorted import *

def choose_random_indices(test_array):
	index1 = random.randint(0,len(test_array)-1)
	index2 = random.randint(index1+1, len(test_array)-1)
	return (index1, index2)	

def check_value_change(test_array, index1, index2):
	pass

class TestAlmost_Sorted(unittest.TestCase):

	def setUp(self):
		# make test_array
		self.test_array = [random.randint(0,10) for i in range(10)]
		self.test_array1 = [random.randint(0,10) for i in range(10)]

	def test_swap_function(self):
		
		index1, index2 = choose_random_indices(self.test_array)
		value1_before = self.test_array[index1]
		value2_before = self.test_array[index2]
		swap(self.test_array, index1, index2)
		value1_after = self.test_array[index1]
		value2_after = self.test_array[index2]

		self.assertEqual(value1_before, value2_after)
		self.assertEqual(value2_before, value1_after)

	def test_reverse_function(self):
		index1, index2 = choose_random_indices(self.test_array1)

		sub_array_before = self.test_array1[index1:index2+1]
		reverse(self.test_array1, index1, index2)
		sub_array_after = self.test_array1[index1:index2+1]

		self.assertEqual(sub_array_after == sub_array_before[::-1], True)
		
		

	def test_almost_sorted_results(self):
		pass

if __name__ == '__main__':
	unittest.main()