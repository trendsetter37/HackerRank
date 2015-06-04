def count(array, n):
    result = [0] * 100

    for num in array:
        
        result[num] += 1
        
    for i in result:
        print(i, end= ' ')

if __name__ == '__main__':
    size = int(input())
    array = [ int(i) for i in input().split()]

    count(array, size)