def insertionSort2(alist):
    for index in range(1, len(alist)):
        position = index
        currentValue = alist[position]
        
        while position > 0 and alist[position-1] > currentValue: 
         
            alist[position] = alist[position-1]
            print(' '.join([str(i) for i in alist]))
            position -= 1
        alist[position] = currentValue
    print(' '.join([str(i) for i in alist]))
    return alist

def insertionSort(ar):
    ''' ar is sorted up to the last element '''
    length = len(ar)
    V = ar[length-1]
    
    for i in range(length-1,0
                   , -1):
        ''' we are counting down here ''' 
        print(i)
        if ar[i-1] > V: 
            
            print(V)# looking at the next to last number or not V
            ar[i] = ar[i-1]                 # shifting last value to its place
            
            if i == 1:
                
                ar[0] = V
            print(' '.join([str(i) for i in ar]))
        else:
            print(' '.join([str(i) for i in ar]))
            
    else:
        return ar
            

#end
if __name__ == '__main__':
    size = input()
    ar = [int(i) for i in input().split()]
    insertionSort2(ar)