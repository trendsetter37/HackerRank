
def median(array):
    size = len(array)
    if size & size-1 == 0:    # trick for testing if number is even
        return int((array[size//2]+array[size//2-1])/2)
    else:
        return array[size//2]

if __name__ == '__main__':
    _ = int(input())
    array = sorted([int(i) for i in input().split()])
    print(median(array))