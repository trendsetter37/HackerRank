
''' https://www.hackerrank.com/challenges/maxsubarray '''
def dp(L):
    c_sum = 0
    best_sum = 0
    contig = [-2**31]
    non_contig = [-2**31]
    i = 0
    
    # must loop through all in array
    for num in L:
        value = c_sum + num
        if value > 0:
            if c_sum == 0:
                contig.append(value)           
            c_sum = value
        else:
            contig = [-2**31]
            c_sum = 0            
        # last check
        if c_sum > best_sum:
            best_sum = c_sum
            contig.append(best_sum)
                        
        # non-contig 
        if i == 0:
            val = num
            if val > non_contig[-1]:
                non_contig.append(val)      
        else:
            val = num + non_contig[-1]
            if val > non_contig[-1]:
                non_contig.append(val)
        i += 1
    return map(str, (contig[-1], non_contig[-1]))
             
if __name__ == '__main__':
    test_cases = int(raw_input())
    for i in xrange(test_cases):
        arr_length = int(raw_input())
        array = (int(i) for i in raw_input().split()) # Using generator here so testcase #2 doesn't hurt
        
        print ' '.join(dp(array))