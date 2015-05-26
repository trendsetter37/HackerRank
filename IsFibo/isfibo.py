
import math

def perf_square(n):
    ''' A number is in the fibonacci sequence if and only if 5n**2 + 4 or 5n**2 - 4 is a perfect square '''
    pos = 5*n**2 + 4
    neg = 5*n**2 - 4
    
    return True if math.sqrt(pos) % 1 == 0 or \
                   math.sqrt(neg) % 1 == 0\
                else False

#end 
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        if perf_square(n):
            print("IsFibo")
        else:
            print("IsNotFibo")