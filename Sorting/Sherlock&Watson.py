
def find_new_values(operations, queries, array):    
    result = operations % len(array)
    for i in range(queries):
        idx = int(input())
        print(array[idx-result])

if __name__ == '__main__':
    nkq = [int(i) for i in input().split()]   
    array = [i for i in input().split()]    
    find_new_values(nkq[1], nkq[2], array)