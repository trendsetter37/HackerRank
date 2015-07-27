memoize = {}

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        if n in memoize:
            return memoize[n]
        else:
            return fib(n-1) + fib(n-2)
        
def fibsum(N):
    not_completed = True
    sums = 0
    count = 3
    
    while not_completed:
        value = fib(count)
        if count not in memoize:
            memoize[count] = value
        if value <= N:
            sums += value
        else:
            not_completed = False
        count += 3
    return sums

if __name__ == '__main__':
    T = int(raw_input())
    
    for i in xrange(T):
        N = long(raw_input())
        print fibsum(N)
        