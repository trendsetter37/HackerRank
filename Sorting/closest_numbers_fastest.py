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
    result = []
    for i in sorted(answers):
        if i[0] == MAX_INT:
            result.append(i)
        else:
            break
    return result                     # took shortcut here
 
if __name__ == '__main__':
    n = int(input())
    array = [int(i) for i in input().split()]
    array.sort() # Sorting array inplace
    result = find_smallest_difference(array)
    
    for answer in result:
        print(array[answer[1][0]], array[answer[1][1]], end=' ')
    