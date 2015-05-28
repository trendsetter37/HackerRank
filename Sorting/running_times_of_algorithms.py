def insertionSort(array):
    count = 0
    for i in range(1, len(array)):
        position = i
        currentValue = array[position]
        while position > 0 and array[position-1] > currentValue:
            array[position] = array[position-1]
            count += 1
            position -= 1
        array[position] = currentValue
    print(count)
    return array

if __name__ == '__main__':
    size = int(input())
    insertionSort([int(i) for i in input().split()])