def compute_difference(num1, num2):
    return num2-num1

def find_smallest_difference(sorted_array):
    answers = []
    MAX_INT = 2**63-1
    for i in range(len(sorted_array)-1):
        diff = compute_difference(sorted_array[i], sorted_array[i+1])
        if diff <= MAX_INT:
            answers.append( [diff,(i, i+1)])    # [difference, (indexes of values in sorted_array)]
            MAX_INT = diff
    return [i for i in sorted(answers) if i[0] == MAX_INT]                     # took shortcut here
    
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
		#print(' '.join([str(i) for i in array]))
		quicksort(array, lo, p-1)
		quicksort(array, p+1, hi)
        
if __name__ == '__main__':
    n = int(input())
    array = [int(i) for i in input().split()]
    quicksort(array, 0, len(array)-1) # Sorting array inplace
    result = find_smallest_difference(array)
    
    for answer in result:
        print(array[answer[1][0]], array[answer[1][1]], end=' ')