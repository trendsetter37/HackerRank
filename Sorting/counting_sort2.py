def count(array):
    a = [0] * 100
    
    for i in array:
        a[i] += 1
    return a

def prints(ar):
    for i in range(len(ar)):
        print("{}".format((str(i)+' ') * ar[i]), end='')

if __name__ == '__main__':
    n = int(input())
    ar = [int(i) for i in input().split()]
    prints(count(ar))