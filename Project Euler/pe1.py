def sum35(limit):
    CONST = (3,5,15) # Adding summation of 3 &5 but subtracting 15
    sums = 0
    for constant in CONST:       
        lim = limit//constant if limit%constant != 0 else limit//constant-1
        if constant != 15:            
            sums += constant*lim*(lim+1)/2            
        else:
            sums -= constant*lim*(lim+1)/2
    return sums

if __name__ == '__main__':
    T = int(raw_input()) # number of testcases
    for i in xrange(T):
        n = int(raw_input())
        print sum35(n)