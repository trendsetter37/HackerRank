from collections import Counter


def profit(sizes, order_tup):
    stock = Counter(sizes)
    p = 0
    for order in order_tup:
        if stock[order[0]] > 0:
            p += order[1]
            stock[order[0]] -= 1
    return p
