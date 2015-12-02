BASE_10 = 10
SQUARE = 2


def repunit(n):
    ''' Creates repunits
        R_n = (10^n - 1) / (10 - 1)
        1 = 1, 2 = 11, 3 = 111
    '''
    return (BASE_10**n) / 9


def demlo_numbers(n):
    ''' Converts repunit number to demlo number
        1^2 = 1, 11^2 = 121, 111^2 = 12321
    '''
    return n**SQUARE
