''' Should use permutations because order does matter

    Needs to happen under 10 seconds to avoid timeout on hackerrank '''
import itertools

def dryshark(constraints, array):
    m, r, s = map(int, constraints.split())
    arr = [int(x) for x in array.split(' ')]
    print(arr)
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
        if num == 1:
            print('entered if clause')
            for tup in itertools.permutations(arr, 2):
                check_sum((tup[0],), (tup[1],))
        else:
            print('Entered else clause')
            tuples = list(itertools.permutations(arr, num))  # provides tuples of 2
            #tup_perm = itertools.permutations(tuples, 2)  # will always compare 2
            print(tuples)
    return yes


if __name__ == '__main__':
    print(dryshark('98 44 0', '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1'))
