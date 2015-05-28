def insertionSort(ar):
    for i in range(1,len(ar)): # first position is sorted
        position = i
        currentValue = ar[position]
        
        while position > 0 and ar[position-1] > currentValue:
            ar[position] = ar[position-1]
            position -= 1
        ar[position] = currentValue
        print(' '.join([str(i) for i in ar]))
    return ar

if __name__ == '__main__':
    size =  int(input())
    ar = [int(i) for i in input().split()]
    
    insertionSort(ar)