''' Your task is to print all possible permutations
    of size k of the string in lexicographic sorted order.
'''
from itertools import permutations


def permute(input_string):
    string, length = input_string.split(' ')
    string = ''.join(sorted(list(string)))
    return '\n'.join(
        map(lambda tup: ''.join(tup), list(permutations(string, int(length))))
    )
