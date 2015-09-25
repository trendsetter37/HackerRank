# T(n+2) = (n+1)^2 + (n+2)

def modified_fib(A,B,N):
    n_arr = [A,B]
    for i in xrange(2, N):
        n_arr.append(n_arr[i-2] + n_arr[i-1]**2)
    return n_arr[-1]

if __name__ == '__main__':
    A, B, N = [ int(i)for i in raw_input().split()]
    print modified_fib(A, B, N)