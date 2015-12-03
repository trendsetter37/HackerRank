''' Your task is to print all possible permutations
    of size k of the string in lexicographic sorted order.
'''
from itertools import permutations, combinations


def hacker_output(lis):
    return '\n'.join(map(lambda tup: ''.join(tup), lis))


def permute(input_string):
    string, length = input_string.split(' ')
    length = int(length)
    string = ''.join(sorted(list(string)))
    result = list(permutations(string, length))
    return hacker_output(result)


def combinate(input_string):
    string, length = input_string.split(' ')
    length = int(length)
    string = ''.join(sorted(list(string)))
    result = []
    for i in xrange(1, length + 1):
        result.extend(list(combinations(string, i)))
    return hacker_output(result)
