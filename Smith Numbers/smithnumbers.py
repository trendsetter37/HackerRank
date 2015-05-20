
def primes2(n):
    sums = 0
    d = 2
    while d*d <=n:
        while (n % d) == 0:            
            if len(str(d)) == 1:
                sums += d
            else:
                sums += sum([int(o) for o in str(d)])
            n //= d
        d += 1
    if n > 1:        
        if len(str(n)) == 1:
            sums += n
        else:                 
            sums += sum([int(o) for o in str(n)])    
    return sums		

#end
if __name__ == '__main__':
    number = input() 
    if sum([int(o) for o in number]) == primes2(int(number)):
        print("1")
    else:
        print("0")