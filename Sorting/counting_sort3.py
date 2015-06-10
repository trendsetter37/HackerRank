def count(array):
    result = [0] * 100 # 0 to 99 inclusive  
    for i in array:
        result[i] += 1
    return result

if __name__ == '__main__':
    size = int(input())
    ar = [int(input().split()[0]) for i in range(size)]
    counts = count(ar)
    sums = 0
    for i in range(100):
        sums += counts[i]
        print(sums, end=' ')