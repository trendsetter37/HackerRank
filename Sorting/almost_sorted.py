
def swap(array, index1, index2):
	array[index1], array[index2] = array[index2], array[index1]


def reverse(array, index1, index2):
	
	if index1 > index2:
		return
	
	swap(array, index1, index2)
	reverse(array, index1+1, index2-1)


def almost_sorted(array, size):
	''' need to return values in order to test 

		* Looks like anomalies need to fulfill a%2 and <5'''


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