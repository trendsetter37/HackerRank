def number_of_ways(cents, coins, ways):
    '''
        Example: cents = 4, coins = [1,2,3], ways = [1,0,0,0,0]
        return        ways[cents] = 4
        step 3        [1,1,2,3,4]   [*,*,*,3,4]
        step 2        [1,1,2,2,3]   [*,*,2,2,3]
        step 1        [1,1,1,1,1]   [*,1,1,1,1]
        initial state [1,0,0,0,0]   [1,0,0,0,0]

        '*' represents states that are the same as a latter step.
    '''
    for coin in coins: # Iterate through each coin (previously sorted for this method)
        for i in xrange(coin, cents + 1):
            # go from current coin to the maximum amount of change needed
            ways[i] += ways[i - coin] # Visully this looks like a mini-staircase
    return ways[cents]

if __name__ == '__main__':
    N, M = [int(i) for i in raw_input().split()]
    coins = sorted([int(i) for i in raw_input().split()]) # Tis sorted for a reason
    ways = [1] + [0]*N
    print number_of_ways(N, coins, ways)
