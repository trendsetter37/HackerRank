def partition(array):
    first = []
    second = []
    
    p = int(array.pop(0))
    
    for i in range(len(array)):
        if int(array[i]) > p:
            second.append(array[i])
        else:
            first.append(array[i])
    first.append(str(p)); first.extend(second)
    
    return ' '.join(first)

if __name__ == '__main__':
    size = input()
    print(partition(input().split()))