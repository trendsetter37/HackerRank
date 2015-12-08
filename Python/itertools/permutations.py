'''
    For HackerRank Python Section
    Your task is to print all possible permutations
    of size k of the string in lexicographic sorted order.
'''
from itertools import permutations, \
    combinations, combinations_with_replacement, \
    groupby, product


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


''' Probability class '''


class Acount(object):
    ''' https://www.hackerrank.com/challenges/iterables-and-iterators '''
    count = 0

    def __init__(self, l, k):
        ''' l = list
            k = length of tuples for combinations
        '''
        self.l = l
        self.k = k

    def inc(self):
        self.count += 1

    @property
    def prob(self):
        ''' All possible tuples of length 2 comprising of indices from 1 to 4
            Find the probability that at least one of the K indices selected
            will contain the letter: 'a'.
        '''

        a_indices = []
        indices = []
        for idx, letter in enumerate(self.l):
            if 'a' == letter:
                a_indices.append(idx)
            indices.append(idx)
        a_indices = set(a_indices)
        result = list(combinations(indices, self.k))
        [self.inc() for s in result if len(a_indices & set(s)) > 0]
        return self.count / float(len(result))


def string_compression(string):
    result = [(len(list(g)), int(k)) for k, g in groupby(string)]
    return result


def maximize(lists, M):
    ''' f(x) = x^2
        https://www.hackerrank.com/challenges/maximize-it
        Sample input
        3 1000
        2 5 4
        3 7 8 9
        5 5 7 8 9 10

        Desired Output
        206
    '''

    ls = []
    for l in lists:
        ls.append(map(lambda x: x**2, l))
    return max(map(lambda x: x % M, map(sum, product(*ls))))
