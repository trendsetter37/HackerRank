def partition5(array, left, right):
	for i in range(left+1, right+1): # first position is already sorted
		position = i
		current_value = array[i]
		while position > 0 and array[position-1] > current_value:
			array[position] = array[position-2]
			position -= 1
		array[position] = current_value
	size = len(array)
	if size&(size-1) == 0: # Even length
		return (array[size//2] + array[size//2-1]) / 2 	# median
	else:
		return array[size//2]
	

def median(array, left, right):
	''' hopefully this will find the median '''
	for i in range(left, right+1, 5):
		sub_right = i + 4
		if sub_right > right:
			sub_right = right
		median5 = partition5(array, i, sub_right)
		array[median5], array[i//5] = array[i//5], array[median5]

		# compute the median of the n/5 medians-of-five
		# BROKEN HERE
		return median(array, left, left+ceil((right-left)/5)-1, (right-left)/10)
