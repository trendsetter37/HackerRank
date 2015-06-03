def partition(array, lo, hi):
	pivot_index = hi
	pivot_value = array[pivot_index]
	store_index = lo

	for i in range(lo, hi):
		if array[i] <= pivot_value:
			array[i], array[store_index] = array[store_index], array[i]
			store_index += 1
	array[pivot_index], array[store_index] = array[store_index], array[pivot_index]
	return store_index 


def quicksort(array, lo, hi):
	if lo < hi:
		p = partition(array, lo, hi)
		print(' '.join([str(i) for i in array]))
		quicksort(array, lo, p-1)
		quicksort(array, p+1, hi)
    
if __name__ == '__main__':
    size = int(input())
    ar = [int(i) for i in input().split()]
    quicksort(ar, 0, size-1)