
def swap(array, index1, index2):
	array[index1], array[index2] = array[index2], array[index1]


def reverse(array, index1, index2):
	
	if index1 > index2:
		return
	
	swap(array, index1, index2)
	reverse(array, index1+1, index2-1)


def almost_sorted(array, size):
	''' need to return values in order to test 

		* Looks like anomalies need to fulfill a%2 and <5

		What i did was:
		(1)input the array in vector
		(2)run through the vector from index 1 to len-2 ( leaving the first and last elements)
		(3)At each of these indices check whether it forms an inversion or a reverse inversion. Inversion is if curr > prev && curr > next. Similarly find out reverse inversions, curr < prev && curr < next. I call inversions as dips, and reverse inversions as ups.
		(4)for the first and last elements you can check only the next and prev respectively as they are at the boundary.
		(5)Once you have collected data of these inversions, if you analyze you will see that if reverse has to form a soln, you will have only one dip and one up.
		(6)And if swapping can be soln then there will be 2 dips and 2 ups.
		(7)If you get more than 2 dips and 2ups, it means it can't be solved.
		(8)There are some edge cases which you need to take care of though

		'''


	anomalies = 0
	reverse_count = 0
	anomaly_locations_and_type =[] 

	for i in xrange(1, size-1):
		if array[i] < array[i-1]:
			anomalies += 1
			if array[i] > array[i+1]:
				reverse_count += 1 # only applicable for reversals
		elif array[i] > array[i+1]:
			anomalies += 1
	if anomalies == 0:
		return 'yes'
	elif reverse_count == 0 and anomalies % 2 == 0 and anomalies <5:
		return 'yes\nreversal'
	else:
		return 'no'
#fin

if __name__ == '__main__':
	size = int(input())

	# TODO convert this to a generator for practice
	array = [int(i) for i in input().split()]