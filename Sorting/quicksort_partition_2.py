def partition(array):
    first = []
    second = []
    pivot = []
    
    if len(array) < 2:
        return array
    else:
        p1 = array[0]
        
        for i in array:
            if i > p1:
                second.append(i)
            elif i < p1:
                first.append(i)
            else:
                pivot.append(i)
        first = partition(first)
        second = partition(second)
        print(' '.join([str(i) for i in first+pivot+second]))
        return first + pivot + second

if __name__=='__main__':
    input()
    partition([int(i) for i in input().split()])