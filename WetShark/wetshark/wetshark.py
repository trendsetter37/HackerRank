''' Should use permutations because order does matter

    Needs to happen under 10 seconds to avoid timeout on hackerrank '''
import itertools

def dryshark(constraints, array):
    m, r, s = map(int, constraints.split())
    arr = [int(x) for x in array.split(' ')]
    yes = 0
    def check_sum(A, B):
        # will always receive two subseqs
        nonlocal yes
        sum_a = sum(A)
        sum_b = sum(B)
        calc_r = sum_a + sum_b
        calc_s = sum_a - sum_b
        if calc_r == r and calc_s == s:
            yes += 1
    for num in range(1, len(arr) + 1):
        # check sum
        if num == 1:
            perm = itertools.permutations(arr, 2)
            for tup in perm:
                a = tup[0],
                b = tup[1],
                check_sum(a, b)
        else:
            tuples = itertools.permutations(arr, num)  # provides tuples of 2
            tup_perm = itertools.permutations(tuples, 2)  # will always compare 2
            for tuppy in tup_perm:
                check_sum(tuppy[0], tuppy[1])
    return yes


if __name__ == '__main__':
    print(dryshark('4 5 3', '1 1 1 4'))
