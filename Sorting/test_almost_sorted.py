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

		# Answer yes
		self.test_array12 = [5,6,7,8,9,10]
		self.test_array13 = [23, 44, 46, 47, 55, 60, 89]

		# Answer yes \nswap l r
		self.test_array2 = [3, 3,2,1] # Answer = swap 0 2
		self.test_array11 = [6, 1, 5, 3, 4, 2, 6] # Answer = swap 2 5

		# Answer no
		self.test_array3 = [15, 5, 81, 15, 27, 54, 63, 11, 93, 149, 244, 190, 216, 229, 164, 249]
		self.test_array4 = [4, 20, 15, 70, 3] 
		self.test_array5 = [4, 8, 1, 7, 6] 
		self.test_array6 = [4, 1, 5, 3, 4]
		self.test_array7 = [9, 1, 5, 4, 3, 6, 10, 9, 8, 11] # failing here two swaps needed
		self.test_array8 = [8, 1, 5, 4, 3 ,6,9, 8, 7]

		self.no_arrays = [self.test_array3,self.test_array4,self.test_array5,\
						  self.test_array6,self.test_array7,self.test_array8]

		#Answer yes\nreverse l r
		self.test_array9 = [3, 3, 2, 1] # reverse 1 3 should swap instead
		self.test_array10 = [6, 1, 5, 4, 3, 2, 6] # Answer = reverse 2 5

			
	def test_almost_sorted_when_swap_is_correct_answer(self):
		''' using test_array2, test_array11 & test_array9 '''
		result = almost_sorted(self.test_array2[1::], len(self.test_array2[1::]))
		answer = "yes swap"
		self.assertEqual(almost_sorted(self.test_array2[1::], len(self.test_array2[1::])), answer,\
		 "array: {0}\n{1}\n{2} != {3}".format(2, self.test_array2[1::], result, answer))

		result = almost_sorted(self.test_array11[1::], len(self.test_array11[1::]))
		answer = "yes swap"
		self.assertEqual(almost_sorted(self.test_array11[1::], len(self.test_array11[1::])), answer,\
			"array: {0}\n{1}\n{2} != {3}".format(11, self.test_array11[1::], result, answer))

		result = almost_sorted(self.test_array9[1::], len(self.test_array9[1::]))
		answer = "yes swap"
		self.assertEqual(almost_sorted(self.test_array9[1::], len(self.test_array9[1::])), answer,\
			"array: {0}\n{1}\n{2} != {3}".format(9, self.test_array9[1::], result, answer))
		

	def test_almost_sorted_when_reverse_is_correct_answer(self):
		''' using test_array9 & test_array10 '''
		
		self.assertEqual(almost_sorted(self.test_array10[1::], len(self.test_array10[1::])), 'yes reverse')
		

	def test_almost_sorted_when_no_is_correct_answer(self):
		''' Using: test_arrays 3-8 '''
		print("\n")
		for idx, array in enumerate(self.no_arrays):
			result = almost_sorted(array[1::], len(array[1::]))
			answer = 'no'
			self.assertEqual(result, answer, "failed on array {}: {}\n {} != {}".format(idx+3, array[1::], result, answer))
	

	def test_almost_sorted_when_yes_is_correct_anwer(self):
		''' Using: test_array 12 & test_array 13 '''
		
		self.assertEqual(almost_sorted(self.test_array12, len(self.test_array12[1::])), 'yes')
		self.assertEqual(almost_sorted(self.test_array13, len(self.test_array13[1::])), 'yes')
		
 
if __name__ == '__main__':
	unittest.main()