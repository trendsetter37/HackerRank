
def swap(array, index1, index2):
	array[index1], array[index2] = array[index2], array[index1]


def reverse(array, index1, index2):
	
	if index1 > index2:
		return
	
	swap(array, index1, index2)
	reverse(array, index1+1, index2-1)


def almost_sorted(array):
	pass
#fin

if __name__ == '__main__':
	size = int(input())

	# TODO convert this to a generator for practice
	array = [int(i) for i in input().split()]