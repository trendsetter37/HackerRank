
samples = [[1,2,3,4,5], [1,4,3,2,5], [1,7,6,5,4,3,2,8], [1,2,3,4,5,9,7,8,6]]



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
	
	#anomaly_locations_and_type =[] 
	curr = 0
	prev = 0
	next = 0
	dips = 0
	ups = 0
	answer = ''
	swap_locations = []
	r_locations = []
	zeroes = 0
	ones = 0

	for i in xrange(1, size-1):
		prev = array[i-1]
		curr = array[i]
		next = array[i+1]
		if curr > prev and curr > next: # Forms an inversion or dips or 0
			#[3,2,1]
			swap_locations.append(i)
			zeroes += 1
			dips += 1
		elif curr < prev and curr < next: # Forms a reverse inversion or ups or 1
			#anomaly_locations_and_type.append((i, '1'))
			r_locations.append(i)
			ones += 1
			ups += 1
		elif curr < prev and curr > next and size == 3:
			return 'yes swap'

	if dips ==1 and ups ==1 and size != 4:
		answer = 'yes reverse'
	elif dips == 2 and ups == 2:
		answer = 'yes swap'
	elif dips == 0 and ups == 0:
		answer = 'yes'
	else:
		answer = 'no'
	return answer

#fin

if __name__ == '__main__':
	size = int(input())

	# TODO convert this to a generator for practice
	array = [int(i) for i in input().split()]