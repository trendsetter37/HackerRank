def counting_sort(array):
    helper = {}
    size = len(array)//2
    for idx, i in enumerate(array):
        if i[0] in helper: 
            if idx < size:
                helper[i[0]].append('-')
            else:        
                helper[i[0]].append(i[1])
        else:
            if idx < size:
                helper[i[0]] = []; helper[i[0]].append('-')
            else:
                helper[i[0]] = []; helper[i[0]].append(i[1])      
    return helper
        


if __name__ == '__main__':
    size = int(input())
    array = [input().split() for i in range(size)]
    result = counting_sort(array)
    
    for i in range(len(result)):
        for thing2 in result[str(i)]:
            print(thing2, end=" ")