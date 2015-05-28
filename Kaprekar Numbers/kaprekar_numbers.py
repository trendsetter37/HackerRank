# stay with base 10 for this

def k_check(num):
    ''' return true of false depending on whether or not
        the num is a keprakar number '''  
 
    if num == 1:       
        return True
    elif len(str(num)) == 1 and num != 9: 
        return False
    else:
        num_str = str(num**2)   
        split = len(num_str)//2
        
        l = num_str[0:split:]  
        r = num_str[-len(num_str)//2::] 
        
        if(int(l) + int(r) == num):   
            return True
        else:
            return False

def kaprekar():
    p = int(input())    #lower bounds
    q = int(input())    #upper bounds
    INVALID_RANGE = True
    
    for i in range(p, q+1):       
        if k_check(i):
            INVALID_RANGE = False
            if i != q:
                print(i, end=' ')
            else:
                print(i)
    else:
        if INVALID_RANGE:
            print("INVALID RANGE")
            
   
#end
if __name__ == '__main__':
    kaprekar()