def unfair(n, k, n_list):
    ''' need to get the numbers with the least amount between them'''
    unfairness = 2**63-1
    for idx, num in enumerate(n_list[:-(k+1)]):
        f = abs(num-n_list[idx+(k-1)])
        if f < unfairness: unfairness = f;
        
    return unfairness
        
    
    
# 1335 to testcase2
#end
if __name__ == '__main__':
    N = int(input()) # number of numbers
    K = int(input()) # How many to choose 
    numbers = []
    
    for i in range(int(N)):
        numbers.append(int(input()))
        
    
    
                
    numbers.sort() # Sort first
    
    print(unfair(N,K,numbers))