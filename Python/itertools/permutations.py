'''
    For HackerRank Python Section
    Your task is to print all possible permutations
    of size k of the string in lexicographic sorted order.
'''
from itertools import permutations, combinations, combinations_with_replacement


def _hacker_output(lis):
    return '\n'.join(map(lambda tup: ''.join(tup), lis))


def _split_vars(string):
    string, length = string.split(' ')
    return ''.join(sorted(list(string))), int(length)


def permute(input_string):
    string, length = _split_vars(input_string)
    result = list(permutations(string, length))
    return _hacker_output(result)


def combinate(input_string):
    string, length = _split_vars(input_string)
    result = []
    for i in xrange(1, length + 1):
        result.extend(list(combinations(string, i)))
    return _hacker_output(result)


def combinate_with_replace(input_string):
    string, length = _split_vars(input_string)
    return _hacker_output(list(combinations_with_replacement(string, length)))
