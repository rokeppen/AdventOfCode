from numpy import array
from itertools import takewhile, count


def reduce(v, f):
    for i in takewhile(lambda _: len(v) > 1, count()):
        v = v[v[:, i] == f(v[:, i], key=lambda c: ((v[:, i] == c).sum(), c))]
    return int(''.join(v[0]), 2)


def get_product():
    values = array([list(x.strip()) for x in open("input.txt")])
    return reduce(values, min) * reduce(values, max)


if __name__ == '__main__':
    print(get_product())
