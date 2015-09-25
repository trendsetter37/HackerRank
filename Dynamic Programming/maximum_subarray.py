
''' https://www.hackerrank.com/challenges/maxsubarray '''
def dp(L):
    max_so_far = max_ending_here = -2**31 # contig logic works
    non_contig = [L[0]] # accounting for negative arrays

    for i in xrange(len(L[0::])):
        max_ending_here = max(L[i], max_ending_here + L[i])        
        max_so_far = max(max_so_far, max_ending_here) 
        # non-contiguous logic
        if i != 0:
            non_contig.append(max(non_contig[-1], non_contig[-1] + L[i]))   
    return map(str, (max_so_far, non_contig[-1]))

if __name__ == '__main__':
    test_cases = int(raw_input())
    for i in xrange(test_cases):
        arr_length = int(raw_input())
        array = (int(i) for i in raw_input().split()) # Using generator here so testcase #2 doesn't hurt
        
        print ' '.join(dp(array))